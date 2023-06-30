14:51 2023/6/29
(предыдущее состояние файла похерило сбоем)

Чтобы сделать подписи к БАРПЛОТУ, есть метод
	Axes.bar_label(container, labels=None, *, fmt='%g', label_type='edge', padding=0, **kwargs)

Чтобы его использовать, нужны:
а) Axes - что очевидно
б) объект container - что совершенно неочевидно		(что это такое - рассмотрю ниже)
	ладно бы контейнер передавался опционально, пущей гибкости заради. 
	Нет, он безальтернативно обязателен.
Так и тянет написать для этого какую-нибудь обертку
в) labels - массив меток. Опционален, но очевидно - если не передан, используются данные, ассоциированные с БАР-ами.
	labels	array-like, optional
	... If not given, the label texts will be the data values formatted with fmt.



Кто такой контейнер
https://matplotlib.org/stable/api/container_api.html
Container for the artists of bar plots (e.g. created by Axes.bar).
The container can be treated as a tuple of the patches themselves. Additionally, you can access these and further parameters by the attributes.

Т.е. это такая прослойка между Axes и самими БАР-ами, включающая в себя сами БАР-ы и некоторые их свойства.

У Axes есть атрибут containers - список отдельных "контейнеров".
В случае простого Axes - контейнер в списке 1.
	ax.containers[0].__dict__.keys()
'patches', 'errorbar', 'datavalues', 'orientation', '_callbacks', '_remove_method', '_label', 'stale'
	'patches': сами БАР-ы - объекты "прямоугольник" - matplotlib.patches.Rectangle
		patches - родительский класс "прямоугольника" - "объект с двумя цветами - заливки и рамки"
		Patches are Artists with a face color and an edge color.
	'datavalues': массив (нампаевский) ассоциированных с ними значений
	'_label': get_label()	Return the label used for this artist in the legend. В простом Axes - пустует. Посмотрю как у сложного.


Таким образом, чтобы просто показать подписи у самого простого графика (пускай даже одного из группы), надо ввести такое:
	sns_figure.axes[1].bar_label(sns_figure.axes[1].containers[0])

Я кое-как научился побеждать вот эту вечную избыточность у пандов, и тут снова мне она.
Оно еще и возвращает:	A list of Text instances for the labels.
Т.е. его не встроить в цепочку.






Вот тут относительно простые примеры, как с этим обращаться
https://www.geeksforgeeks.org/how-to-show-values-on-seaborn-barplot/
