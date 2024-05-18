# This Python file uses the following encoding: utf-8
import sys
import test
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel,QVBoxLayout, QWidget
from PySide6.QtGui import QPixmap  # Importar QPixmap
from PySide6.QtWidgets import QTreeWidgetItem



# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

class MainWindow(QMainWindow):
    def onItemClicked(self, item, column):
        def set_imagen(self, nombre_de_imagen):
                # Construir la ruta completa de la imagen.
                ruta_imagen = os.path.join('img', nombre_de_imagen)
                pixmap = QPixmap(ruta_imagen)
                if pixmap.isNull():
                    print("La imagen no se pudo cargar o es inválida.")
                    pixmap = QPixmap('img/pokedex.jpg')
                    pixmap = pixmap.scaled(self.ui.imagen.width(), self.ui.imagen.height(), )
                    self.ui.imagen.setPixmap(pixmap)
                    return


                pixmap = pixmap.scaled(self.ui.imagen.width(), self.ui.imagen.height(), )
                self.ui.imagen.setPixmap(pixmap)
        self.ui.propiedades.setText("")
        set_imagen(self,item.text(column))
        txt_propiedades = test.obtenerPropiedades(item.text(column))
        txt_propiedades = txt_propiedades.strip("[]")
        propiedades = txt_propiedades.split(',')
        texto_con_saltos = "\n".join(propiedades)
        self.ui.propiedades.setText(texto_con_saltos)
        txt_desc= test.obtenerDescripcion(item.text(column))
        self.ui.descripcion.setText(txt_desc)

    def onItemClicked2(self, item):
        self.ui.todasclases.setText("")
        txt = test.obtenerClasesPorPropiedad(item.text())
        txt = txt.strip("[]")
        propiedades = txt.split(',')

        # Crear HTML para estructurar el texto en columnas
        num_columnas = 2
        html_texto = '<table style="width:100%;border-spacing: 5px;">'
        for i in range(0, len(propiedades), num_columnas):
            html_texto += "<tr>"
            for j in range(num_columnas):
                if i + j < len(propiedades):
                    html_texto += f"<td style='vertical-align: top;padding:10px;'>{propiedades[i + j].strip()}</td>"
            html_texto += "</tr>"
        html_texto += "</table>"

        self.ui.todasclases.setStyleSheet("QLabel { vertical-align: top; }")

        self.ui.todasclases.setText(html_texto)



    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.tree_clases.itemClicked.connect(self.onItemClicked)
        self.ui.listPropiedades.itemClicked.connect(self.onItemClicked2)



        pixmap = QPixmap('img/pokedex.jpg')
        self.ui.imagen.setPixmap(pixmap)
        self.ui.imagen.setScaledContents(True)

        # Manejo del TreeWidget
        self.ui.tree_clases.setColumnCount(1)
        root = QTreeWidgetItem(self.ui.tree_clases)


        root.setText(0,'Tipos Pokémon')

        def extraer_pokemones(cadena):
            cadena_limpia = cadena.strip("[] ")
            lista_pokemon = [pokemon.strip() for pokemon in cadena_limpia.split(",")]

            if lista_pokemon and lista_pokemon[-1].endswith(']'):
                lista_pokemon[-1] = lista_pokemon[-1][:-1].strip()

            return lista_pokemon

        # Lista de tipos de Pokémon
        tipos_pokemon = ['Agua','Fuego','normal','Lucha', 'siniestro', 'Hada', 'Psiquico', 'Roca', 'Tierra','Veneno', 'Planta', 'Volador', 'electrico']


        for tipo in tipos_pokemon:
            nodo_tipo = QTreeWidgetItem(root)
            nodo_tipo.setText(0, f'Tipo {tipo}')

            resultado = test.obtenerClasesPorPropiedad(f"tipo({tipo.lower()})")
            lista_pokemon = extraer_pokemones(resultado)

            for nombre_pokemon in lista_pokemon:
                nodo_pokemon = QTreeWidgetItem(nodo_tipo)
                nodo_pokemon.setText(0, nombre_pokemon)

        def extraer_propiedades(cadena):
            cadena_limpia = cadena.strip("[] ")
            lista_propiedad = [prop.strip() for prop in cadena_limpia.split(",")]
            if lista_propiedad and lista_propiedad[-1].endswith(']'):
                lista_propiedad[-1] = lista_propiedad[-1][:-1].strip()
                return lista_propiedad
        lista_propiedades = test.obtenerTodaPropiedad()
        lista_propiedades = extraer_propiedades(lista_propiedades)
        propiedades_agregadas = set()
        for propiedad in lista_propiedades:
            if propiedad not in propiedades_agregadas:
                self.ui.listPropiedades.addItem(propiedad)
                propiedades_agregadas.add(propiedad)





if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())





