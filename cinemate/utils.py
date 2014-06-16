# coding=utf-8
"""
    Модуль содержит:
    метакласс :class:`.CommonMeta` для реализации служебных методов;
    - класс :class:`.BaseCinemate` от которого наследуются все остальные
      классы проекта;
    - классы :class:`.BaseImage` и :class:`.BaseSlug` в которые вынесен общий
      код для :class:`person.Photo`, :class:`movie.Poster`,
      :class:`movie.Country`, :class:`movie.Genre`;
    - декоратор :func:`require`, который проверяет у экземпляра класса наличие
      указаных аттрибутов;
    - функции :func:`parse_date`, :func:`parse_datetime` для разбора дат и
      времени в формате ISO.

"""
from datetime import datetime
from functools import wraps
from six import add_metaclass, iteritems, PY2


class CommonMeta(type):
    """ Метакласс для реализации __служебных_методов__.
    """
    def __new__(mcs, name, bases, attrs):
        method = attrs.get('__unicode__')
        if method:
            to_str = lambda x: PY2 and method(x).encode('utf-8') or method(x)
            attrs.setdefault('__str__', to_str)
            attrs.setdefault('__repr__', to_str)
        return super(CommonMeta, mcs).__new__(mcs, name, bases, attrs)


@add_metaclass(CommonMeta)
class BaseCinemate(object):
    """ От этого класса наследуются все остальные классы проекта.
    """


class BaseImage(BaseCinemate):
    fields = ('small', 'medium', 'big')

    def __init__(self, small, medium, big):
        self.small = small
        self.medium = medium
        self.big = big

    @classmethod
    def from_dict(cls, dct):
        """ Изображение из словаря, возвращаемого API.

        :param dct: словарь, возвращаемый API
        :type dct: :py:class:`dict`
        :return: изображение
        :rtype: :class:`{module_name}.{class_name}`
        """.format(
            module_name=cls.__module__,
            class_name=cls.__name__,
        )
        if dct is None:
            return
        fields = {k: dct.get(k).get('url') for k in cls.fields if k in dct}
        return cls(**fields)

    def __unicode__(self):
        sizes = '/'.join(k for k, v in sorted(iteritems(self.__dict__)) if v)
        return '<{class_name} {sizes}>'.format(
            class_name=self.__class__.__name__,
            sizes=sizes,
        )


class BaseSlug(BaseCinemate):
    def __init__(self, name, slug=None):
        self.name = name
        self.slug = slug or self.slug_by_name(name)

    @classmethod
    def from_dict(cls, dct):
        """ Задать объект из словаря, возвращаемого API.

        :param dct: словарь, возвращаемый API
        :type dct: :py:class:`dict`
        :return: объект
        :rtype: :class:`{module_name}.{class_name}`
        """.format(
            module_name=cls.__module__,
            class_name=cls.__name__,
        )
        name = dct.get('name')
        slug = dct.get('slug', cls.slug_by_name(name))
        return cls(name=name, slug=slug)

    @classmethod
    def slug_by_name(cls, name):
        """ Получение slug объекта по его названию на русском языке.

        :param name: имя объекта на русском языке
        :return: slug объекта
        :rtype: :py:class:`str`
        """
        finder = (slug for slug, rus in iteritems(cls.mapping) if rus == name)
        return next(finder, None)

    def __unicode__(self):
        return '<{class_name}: {name}>'.format(
            class_name=self.__class__.__name__,
            name=self.slug or self.name,
        )


# noinspection PyPep8Naming
class require(object):
    """ Декоратор проверяет наличие указанных атрибутов у объекта cinemate.
    """
    def __init__(self, *attr_names):
        """
        :param attr_names: имена требуемых аттрибутов
        :type attr_names: :py:class:`str` or :py:class:`tuple`
        """
        self.attr_names = attr_names

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            """ Декорируемая функция.

            :param args: неименованные параметры декорируемой функции
            :type args: :py:class:`tuple`
            :param kwargs: именованные параметры декорируемой функции
            :type kwargs: :py:class:`dict`
            """
            cinemate = __get_cinemate__(args[0])  # args[0] == self or cls
            if not all(getattr(cinemate, a, None) for a in self.attr_names):
                msg = '{attr} required to use {cls}.{method} method'.format(
                    attr=', '.join(self.attr_names),
                    cls=args[0].__class__.__name__,
                    method=func.__name__
                )
                raise AttributeError(msg)
            return func(*args, **kwargs)
        return wrapper


def __get_cinemate__(instance):
    """ Получение объекта cinemate хранящегося в аттрибутах.

    :param instance: экземпляр какого-нибудь класса
    :return: объект cinemate
    :raises AttributeError: Вызывается, если объект не содержит
        требуемых полей или экземпляра cinemate
    """
    if hasattr(instance, 'cinemate'):
        return getattr(instance, 'cinemate')
    elif instance.__class__.__name__ == 'Cinemate':  # avoid cycle imports
        return instance
    else:
        raise AttributeError('Object has not cinemate attribute')


def parse_datetime(source):
    """ Парсинг дат и времени формата ISO. Например: 2011-04-09T15:38:30

    :param source: исходная строка с датой и временем
    :type source: :py:class:`str`
    """
    if not source:
        return
    return datetime.strptime(source, '%Y-%m-%dT%H:%M:%S')


def parse_date(source):
    """ Парсинг дат формата 2011-04-07

    :param source: исходная строка с датой
    :type source: :py:class:`str`
    """
    if not source:
        return
    return datetime.strptime(source, '%Y-%m-%d')
