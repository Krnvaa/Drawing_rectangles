# Drawing_rectangles
[![Build, Test](https://github.com/Krnvaa/Drawing_nested_rectangles/actions/workflows/python-app.yml/badge.svg)](https://github.com/Krnvaa/Drawing_nested_rectangles/actions/workflows/python-app.yml)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/Krnvaa/Drawing_rectangles?color=salmon)
[![License: MIT ](https://img.shields.io/badge/License-MIT-fuchsia.svg)](https://opensource.org/licenses/MIT)
## Лабораторная работа по дисциплине "Компьютерная графика" №1. 
### Демонстрация выполнения работы программы
<img src="https://github.com/Krnvaa/Drawing_rectangles/blob/main/gif/gif.gif" width="700" height="500"> </img>
# Описание задачи
Вариант 7. Требовалось написать программу, которая выводила бы на экран вложенные прямоугольники. При этом каждый очередной прямоугольник должен выводиться при нажатии клавиши Enter, а при нажатии клавиши ‘D’ убирался бы последний построенный прямоугольник. Выход по ESC. Прямоугольники должны выводиться с заданными шагами уменьшения размера его сторон hx, hy.
## Программа реализована на языке:

| Язык | Интерпретатор/Версия | Среда разработки | 
| ------ | ------ | ------ |
| Python | Python / w64 3.9 | PyCharm 2022 3.2 |

## Используемые библиотеки:
* tkinter - для создания графического пользовательского интерфейса (GUI)
* unittest - для написания и выполнения тестов

## Описание возможностей :
- Ввод параметров hx, hy для уменьшения длин сторон прямоугольнка;
- Валидация полей (проверка на ввод отрицательных значений, букв и других недопустимых символов);
- Построение каждого последующего вложенного прямоугольника при нажатии клавиши Enter;
- Удаление последнего построенного прямоугольника при нажатии клавиши D;
- Выход из программы при нажатии клавиши Esc.

## Установка и запуск
1. ```git clone https://github.com/Krnvaa/Drawing_rectangles.git```
2. ```cd <project_folder>```
3. ```python main.py```
