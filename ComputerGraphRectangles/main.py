import tkinter as tk
from ComputerGraphRectangles.input_validation import validate_input


class DrawingRectangles:
    """
    Класс DrawingRectangles для построения и удаления прямоугольников в графическом интерфейсе с использованием библиотеки Tkinter.

     Атрибуты:
     root (tk.Tk): Основное окно графического интерфейса.
     width_canvas (int): Ширина холста для отрисовки прямоугольников.
     height_canvas(int): Высота холста для отрисовки прямоугольников.
     canvas (tk.Canvas): Холст для рисования прямоугольников.
     error_label (tk.Label): Метка для вывода сообщений об ошибках.
     hx_entry (tk.Entry): Поле ввода для величины hx.
     hy_entry (tk.Entry): Поле ввода для величины hy.
     rectangles (list): Список созданных прямоугольников на холсте.
     x, y (int): Текущие значения длин сторон для создания новых прямоугольников.
     hx_increment, hy_increment (int): Значение шага, на которое уменьшаются стороны x, y  при отрисовки
    каждого нового прямоугольника.
    last_deleted_x, last_deleted_y : Последние удаленные значения x и y.

    Методы:
    can_draw_rectangle(x, y)
        Проверяет, можно ли нарисовать прямоугольник с заданными длинами сторон.
    draw_rectangle()
        Рисует прямоугольник на холсте с текущими значениями hx и hy.
    delete_rectangle()
        Удаляет последний нарисованный прямоугольник и сохраняет значения x и y последнего удаленного прямоугольника.
    on_key_press(event)
        Обработчик событий клавиш, реагирующий на Enter (для рисования), "d" (для удаления) и Escape (для закрытия).
    run()
        Запускает основной цикл Tkinter для работы с интерфейсом.
    """

    def __init__(self, root):
        self.root = root
        root.title("Лабораторная работа 1 вариант 7")
        self.width_canvas = 600
        self.height_canvas = 600
        self.canvas = tk.Canvas(root, width=self.width_canvas, height=self.height_canvas)
        self.canvas.pack(side=tk.LEFT)
        input_frame = tk.Frame(root)
        input_frame.pack(side=tk.RIGHT, padx=10, pady=10)
        data_label = tk.Label(input_frame, text="Введите данные и нажмите enter для отрисовки")
        data_label.grid(row=0, columnspan=4, padx=5, pady=5)
        self.error_label = tk.Label(input_frame, fg="red")
        self.error_label.grid(row=4, columnspan=2, padx=5, pady=5)
        validate_input_cmd = root.register(lambda P: validate_input(P, self.error_label))
        hx_label = tk.Label(input_frame, text="Величина hx:")
        hx_label.grid(row=2, column=0, padx=5, pady=5)
        self.hx_entry = tk.Entry(input_frame, validate="key")
        self.hx_entry.config(validatecommand=(validate_input_cmd, "%P"))
        self.hx_entry.grid(row=2, column=1, padx=5, pady=5)
        hy_label = tk.Label(input_frame, text="Величина hy:")
        hy_label.grid(row=3, column=0, padx=5, pady=5)
        self.hy_entry = tk.Entry(input_frame, validate="key")
        self.hy_entry.config(validatecommand=(validate_input_cmd, "%P"))
        self.hy_entry.grid(row=3, column=1, padx=5, pady=5)
        self.rectangles = []
        self.x = None
        self.y = None
        self.hx_increment = None
        self.hy_increment = None
        self.last_deleted_x= None
        self.last_deleted_y=None
        root.bind("<Key>", self.on_key_press)

    def can_draw_rectangle(self, x, y):
        """
        Проверяет, можно ли нарисовать прямоугольник с заданными координатами.

        Ключевые аргументы:
        - x (int): Ширина прямоугольника.
        - y (int): Высота прямоугольника.

        Возвращаемое значение:
        bool: True, если прямоугольник можно нарисовать, иначе False.

        Описание:
        Проверяет, можно ли нарисовать прямоугольник с заданными значениями x, y. Выполняется сравнение
        значения длин сторон x, y с минимальным допустимым размером сторон прямоугольника (это 0). Если x и y больше
        минимального размера, функция возвращает True, что означает, что прямоугольник можно нарисовать. В противном
        случае возвращается False.
        """

        min_size = 0
        if min_size < x and min_size < y:
            return True
        else:
            return False

    def draw_rectangle(self):
        """
        Отвечает за рисование прямоугольника на холсте с текущими значениями длин сторон. Она также выполняет ряд
        операций, связанных с обновлением параметров и обработкой ошибок.

         Описание:
         Сначала проверяется, был ли ранее удален прямоугольник. Если да, то значения x и y восстанавливаются из
         сохраненных предыдущих значений, а сохраненные значения обнуляются. Вызывается метод, который проверяет, можно ли
         рисовать прямоугольник с текущими значениями x и y. Если условия выполняются (прямоугольник можно нарисовать), то:
         Рассчитываются координаты углов прямоугольника (x1, y1, x2, y2) и создается прямоугольник на холсте.
         Созданный прямоугольник добавляется в список отрисованных прямоугольников. Значения x и y уменьшаются на значения
         hx_increment и hy_increment  соответственно, что обеспечивает последующую отрисовку прямоугольников с уменьшенными
         размерами. Если условие для рисования прямоугольника не выполняется (прямоугольник нельзя нарисовать), то на метке
         выводится сообщение об ошибке: "Прямоугольник еще меньше построить уже нельзя".
         """

        if self.x is None:
            self.x = self.width_canvas - 10
        if self.y is None:
            self.y = self.height_canvas - 10
        if self.hx_increment is None:
            self.hx_increment = int(self.hx_entry.get())
        if self.hy_increment is None:
            self.hy_increment = int(self.hy_entry.get())
        self.hx_entry.delete(0, tk.END)
        self.hy_entry.delete(0, tk.END)
        self.hx_entry.config(state=tk.DISABLED)
        self.hy_entry.config(state=tk.DISABLED)
        if self.last_deleted_x is not None and self.last_deleted_y is not None:
            self.x = self.last_deleted_x
            self.y = self.last_deleted_y
            self.last_deleted_x = None
            self.last_deleted_y = None
        if self.can_draw_rectangle(self.x, self.y):
            x1 = (self.width_canvas - self.x) / 2
            y1 = (self.height_canvas - self.y) / 2
            x2 = x1 + self.x
            y2 = y1 + self.y
            rectangle = self.canvas.create_rectangle(x1, y1, x2, y2)
            self.rectangles.append(rectangle)
            self.x -= self.hx_increment
            self.y -= self.hy_increment
        else:
            self.error_label.config(text="Прямоугольник еще меньше построить уже нельзя")

    def delete_rectangle(self):
        """
        Удаляет последний нарисованный прямоугольник с холста.

        Описание:
        Проверяет, есть ли прямоугольники на холсте. Если список с прямоугольниками содержит хотя бы один элемент, выполняется
        удаление последнего прямоугольника. А именно сначала получает координаты углов последнего прямоугольника с холста.
        Вычисляет разницу между координатами углов для определения размеров сторон удаленного прямоугольника. Сохраняет
        размеры удаленного прямоугольника и проверяет, можно ли рисовать новый прямоугольник с такими размерами. В случае
        успешного удаления, метка `error_label` очищается от предыдущего сообщения об ошибке.

        """
        if len(self.rectangles) > 0:
            last_rectangle = self.rectangles[-1]
            x1, y1, x2, y2 = self.canvas.coords(last_rectangle)
            self.last_deleted_x = x2 - x1
            self.last_deleted_y = y2 - y1
            if self.can_draw_rectangle(self.last_deleted_x, self.last_deleted_y):
                self.error_label.config(text="")
            self.canvas.delete(last_rectangle)
            self.rectangles.pop()

    def on_key_press(self, event):
        """
         Обработчик событий клавиатуры для реакции на клавиши Enter, D и Escape.

         Ключевые аргументы:
         event (tk.Event): Событие клавиатуры.

         Описание:
         Обрабатывает события клавиатуры. Если пользователь нажимает клавишу Enter, то вызывается draw_rectangle() для
         отрисовеки вложенного треугольника. Если пользователь нажимает клавишу D (вне зависимости от регистра), то
         вызывается delete_last_rectangle() для удаления последнего треугольника. Если пользователь нажимает клавишу Escape,
         то окно приложения закрывается

        """
        if event.keysym == "Return":
            self.draw_rectangle()
        elif event.keysym == "d":
            self.delete_rectangle()
        elif event.keysym == "Escape":
            self.root.destroy()

    def run(self):
        """
        Запускает главный цикл приложения.

        Описание:
        Эта функция запускает главный цикл приложения, который обрабатывает события и отображает графическиц интерфейс на экране.
        Вызывается для запуска приложения после его инициализации.
        """
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingRectangles(root)
    app.run()