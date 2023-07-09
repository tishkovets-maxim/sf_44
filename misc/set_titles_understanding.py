# Создаем словарь args, куда записываем имена столбцов исходного датафрейма, соответствующие "строкам" и "столбцам" фасетгрида, под именами row_var, col_var
args = dict(row_var=self._row_var, col_var=self._col_var)


# Establish default templates
# Если шаблона передано не было, задаем ШАБЛОН по умолчанию, в моем случае {col_var} = {col_name}

# дальше делаем +- одно и то же, в двух вариантах в зависимости от определенности переменной self._margin_titles
# я такую не заполнял, поэтому иду сразу во второй блок (хотя первый выглядит проще)


# Проверяем заполненность "столбцов" и "строк"
# Так они живут внутри объекта facetgrid:
self._row_var		имя столбца датафрейма под "строки"
self.row_names		уникальные значения этого столбца, они же имена "строк"

self._col_var		имя столбца датафрейма под "столбцы"
self.col_names		уникальные значения этого столбца, они же имена "столбцов"


if (self._row_var is not None) and (self._col_var is not None):
    ...
elif self.row_names is not None and len(self.row_names):
    ...
# А вот и мой случай - когда есть только "столбцы"
#	(проверяем, что переменная col_names а) задана, б) итерируется)
#	А то мало ли, вдруг туда какую-то неитерируемую чушь занесло

elif self.col_names is not None and len(self.col_names):

    for i, col_name in enumerate(self.col_names):
        args.update(dict(col_name=col_name))
        title = template.format(**args)
        # Index the flat array so col_wrap works
        self.axes.flat[i].set_title(title, **kwargs)


Перебираем col_names, так что на каждой итерации col_name - текущий элемент, i - номер текущего элемента
1. Записываем текущий элемент в args под именем "col_name"
2. Формируем строку title, так что template заполняется знакоместами из args
	а там у нас - только col_var и col_name
	под что-то другое места НЕ предусмотрено.
	это НЕ f-string, это Format Specification Mini-Language
3. Назначаем строку title заголовком соответствующего Axes
	(причем Axes) сплющиваем, "чтобы работал col_wrap"
	self.axes.flat
flat - СВОЙСТВО нампаевского массива, возвращающее flatiter - специальный итератор, перебирающий конечные массива, представленного в "плоском" (одномерном) виде


В моем случае - это действие избыточно
		sns_figure.axes.__class__   # numpy.ndarray
		sns_figure.axes.shape       # (6,)
Я не знаю, было, будет или в иных условиях возможна другая размерность у axes, но логика ясна


Отсюда же мы узнаем еще один факт: у Facetgrid нету какой-то определенной специальной сущности, обволакивающей отдельные графики.
Есть инкорпорированная Figure, есть "ярлык" на Axes этой Figure, есть всякие собственные объекты вроде col_names
Но общей сущности в которой вместе были бы axes.flat[i] и col_names[i], чтобы можно было сделать 
так:
for facet in sns_figure.facets:
	facet.set_title (f"{facet.col_name} чего-то там {какая-нибудь еще переменная}")
нет



19:50 2023/6/28
for (i, ax) in enumerate(sns_figure.axes.flat):
    print (ax.title.__class__)

<class 'matplotlib.text.Text'>
...

Т.е. title - поле не просто string, а именно матплотлибовский Text, у которого есть собственно текстовая составляющая, плюс координаты (и надо полагать, что-то еще)

