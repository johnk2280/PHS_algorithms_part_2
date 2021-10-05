# Высшая школа программирования Сергея Бобровского
##  Второй курс по алгоритмам/структурам данных.
### Деревья

В классе **SimpleTree** нам потребуются:
- добавить текущему узлу (первый параметр метода добавления узла) новый узел (второй параметр метода добавления узла) в качестве дочернего (тест: проверяем наличие добавленного узла);
- удалить некорневой узел (удаляется узел вместе со всем поддеревом) (тест: проверяем отсутствие удалённого узла и его потомков);
- последовательно обойти всё дерево и сформировать список всех узлов в произвольном порядке;
- найти список подходящих узлов по заданному значению (тест: проверяем результат с тестовым списком);
- переместить некорневой узел дочерним узлом в другое место дерева (вместе с его поддеревом), для чего воспользуйтесь предыдущими методами (тест: проверяем, что узел отсутствует там где был исходно и появился в новом месте);
- подсчитать общее количество узлов в дереве, и количество листьев (тест: проверяем на контрольном дереве количество узлов и листьев).

Также напишите метод, который перебирает всё дерево и прописывает каждому узлу его уровень.
Придумайте, как лучше организовать поддержку уровня узлов без анализа всего дерева.

### Двоичные деревья поиска.
В задании необходимо реализовать:
- метод поиска (тест: проверяем поиск отсутствующего ключа в двух вариантах (запрошенный ключ добавляем либо левому, либо правому потомку) и поиск присутствующего ключа);
- метод добавления нового узла, задаём добавляемый ключ и соответствующее ему значение (тесты: проверяем исходное отсутствие узла по такому ключу в дереве и его наличие после добавления, в двух вариантах -- левым или правым узлом родителя, а также попытку добавления ключа, которое уже имеется в дереве, в таком случае ничего с деревом не делаем);
- поиск максимального и минимального ключей, начиная с заданного узла (тест, 4 варианта: поиск начиная с корня и поиск начиная с поддерева, ищем максимальный и минимальный ключ);
- метод удаления узла по его ключу (тест: проверяем исходное наличие узла у родителя, его отсутствие после удаления, и результат работы метода).

### Способы обхода дерева.
Задание:
- Реализуйте дополнительный метод обхода дерева WideAllNodes() без параметров для класса из занятия по двоичным деревьям, так, чтобы он реализовывал алгоритм поиска в ширину, начиная с корня.
 - Реализуйте дополнительный метод обхода дерева DeepAllNodes(), начиная с корня, которому задаётся один целый параметр, принимающий значения 0 (in-order), 1 (post-order) и 2 (pre-order). В зависимости от этого параметра метод DeepAllNodes() реализует соответствующую форму алгоритма поиска в глубину.

Эти алгоритмы формируют на выходе стандартный список из объектов BSTNode (List в C#, tuple в Python, ArrayList в Java).

### Двоичные деревья поиска (2).
Мы реализовали двоичное дерево поиска с помощью узлов, которые хранят ссылки на левого и правого потомков. Теперь рассмотрим важную реализацию двоичного дерева в виде массива. Текущая реализация имеет один недостаток: если входные данные упорядочены, то их вставка вступает в конфликт с упорядоченностью внутри дерева -- операции вставки будут требовать сканирования существенной части дерева.

Задание:
- Реализуйте двоичное дерево поиска в виде массива,
- Реализуйте функцию добавления нового узла (фактически, целого ключа), 
- Реализуйте функцию поиска -- не линейно по массиву, а на основе алгоритма из прошлых занятий, через условные "узлы" дерева, только ограничьтесь фиксированным размером массива,
- Заполните полностью дерево глубины N значениями и проверьте тестами работу функций добавления и поиска, а также корректность значений в массиве, реализующем дерево.



Условия:
- Если всё дерево пройдено до его максимальной глубины и все узлы существуют, а совпадения не найдено, поиск возвращает null,
- Если узел (ключ) найден, поиск возвращает его индекс в массиве,
- Если найден незаполненный слот, подходящий для размещения указанного значения (другими словами, если очередной "узел", выбранный в процессе поиска, хранит null), поиск возвращает его индекс в виде отрицательного значения (например, -12).
При использовании такого подхода пользователю класса потребуется учесть частный случай, когда поиск вернёт 0. В таком случае надо дополнительно проверять, пустое ли дерево.

### Строим сбалансированные двоичные деревья поиска.
Задание:
- Напишите функцию GenerateBBSTArray(), которая получает на вход неотсортированный массив, по размеру соответствующий полностью заполненному дереву некоторой положительной глубины, и выдаёт на выходе массив, содержащий структуру сбалансированного BST.
