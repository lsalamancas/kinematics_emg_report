from fpdf import FPDF
import os

''' PDF max and min report, and EMG
This class create a PDF of the...
'''

class PDF_MM(FPDF):

    def __init__(self, p_info, orientation, unit, format): # firstname, lastname, age, pathology, p_id
        super().__init__(orientation, unit, format)
        self.name, self.age, self.pathgy, self.id, _ = p_info
        self.path = os.path.dirname(os.getcwd())


    def header(self):
        self.image(os.sep.join([self.path, 'images', 'roosevelt.png']), 5, 3, 30)

        # HEADER ONLY IN PAGE No 1
        if self.page_no() == 3:
            self.set_font('Helvetica', 'B', 9)
            x1 = 15
            x2 = 155
            center_name = (x1 + x2 + self.get_string_width('DIAGNÓSTICO:')) / 2 - self.get_string_width(self.name) / 2
            center_pathgy = (x1 + x2 + self.get_string_width('DIAGNÓSTICO:')) / 2 - self.get_string_width(self.pathgy) / 2
            self.text(51, 13, 'INSTITUTO ROOSEVELT - LABORATORIO DE ANÁLISIS DE MOVIMIENTO')
            self.text(67.5, 19, 'REPORTE DE MÁXIMOS Y MÍNIMOS (RMS) DEL ACM')
            self.text(x1, 30, 'NOMBRE:')
            self.text(x2, 30, 'EDAD:')
            self.text(15, 36, 'DIAGNÓSTICO:')
            self.text(155, 36, 'ID:')
            self.set_font('Helvetica', 'I', 9)
            self.text(center_name, 30, self.name )
            self.text(center_pathgy, 36, self.pathgy)
            self.text(180, 30, f'{self.age} años' )
            self.text(177, 36, str(self.id))
        else:
            self.set_font('Helvetica', 'B', 10)
            x1 = 27
            x2 = 205
            center_name = (x1 + x2 + self.get_string_width('DIAGNÓSTICO:')) / 2 - self.get_string_width(self.name) / 2
            center_pathgy = (x1 + x2 + self.get_string_width('DIAGNÓSTICO:')) / 2 - self.get_string_width(self.pathgy) / 2
            self.text(87, 13, 'INSTITUTO ROOSEVELT - LABORATORIO DE ANÁLISIS DE MOVIMIENTO')
            self.text(106, 19, 'REPORTE DE MÁXIMOS Y MÍNIMOS (RMS) DEL ACM')
            self.text(27, 30, 'NOMBRE:')
            self.text(205, 30, 'EDAD:')
            self.text(27, 36, 'DIAGNÓSTICO:')
            self.text(205, 36, 'ID:')
            self.set_font('Helvetica', 'I', 9)
            self.text(center_name, 30, self.name)
            self.text(center_pathgy, 36, self.pathgy)
            self.text(230, 30, f'{self.age} años')
            self.text(228, 36, str(self.id))


    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(128)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')


    def pag1(self):
        self.add_page()
        self.image(os.sep.join([self.path, 'images', 'sagittal.png']) , 5, 45, 70, 150)
        self.image(os.sep.join([self.path, 'images', 'transverse.png']) , 140, 45, 70, 150)
        w, h1, h2 = 60, 25, [7, 10, 7, 13]
        x, y, x1 = 75, 47, 210
        y1 = y
        for i, h in zip(range(4), [4, 2, 5, 3]):
            self.image(os.sep.join([self.path, 'images', f'mm_sagittal{i}.png']), x, y, w, h1)
            self.image(os.sep.join([self.path, 'images', f'rng_sagittal{i}.png']), x, y + h1, w, h2[i])
            self.image(os.sep.join([self.path, 'images', f'mm_transverse{i}.png']), x1, y1, w, h1)
            self.image(os.sep.join([self.path, 'images', f'rng_transverse{i}.png']), x1, y1 + h1, w, h2[0])
            y += h1 + h2[i] + h 
            y1 += h1 + h2[0] + 5
        

    def pag2(self):
        self.add_page()
        self.image(os.sep.join([self.path, 'images','frontal.png']) , 75, 55, 75, 120)
        x, y, w, h1, h2 = 155, 57, 60, 25, 8
        for i in range(3):
            self.image(os.sep.join([self.path, 'images',f'mm_frontal{i}.png']), x, y, w, h1)
            self.image(os.sep.join([self.path, 'images',f'rng_frontal{i}.png']), x, y + h1, w, h2)
            y += h1 + h2 + 7


    def pag3(self):
        self.add_page(orientation='P')
        self.image(os.sep.join([self.path, 'images','emg.png']) , 5, 45, 200, 210)
