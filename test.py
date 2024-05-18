import subprocess
import shutil

# swipl --quiet -f data.pl -t com

mainPl = "data.pl" # Archivo principal de prolog sobre la cual se realizan consultas

def consulta(strRegla):
    # Retorna un string, del resultado producido por prolog
    '''
        Por ejemplo
        strRegla = "forall(hombre(X), (write(X), nl))."
        Te dara todos los hombres
    '''

    shutil.copy(mainPl,"out.pl")
    with open("out.pl","a") as f:
        f.write("regla :-" + strRegla)

    comando = "swipl --quiet -f out.pl -t regla"
    result = subprocess.run([comando],shell=True,capture_output=True,text=True)
    return result.stdout

def obtenerPropiedades(pokemon):
	out = consulta("once((propiedadesc({}, L),write(L),nl)).".format(pokemon))
	return out

def obtenerTodaPropiedad():
            out = consulta("todas_propiedades(L),write(L),nl.")
            return out

def obtenerDescripcion(pokemon):
            out = consulta("obtiene_descripcion({},D),write(D),nl.".format(pokemon))
            return out


def obtenerClases():
	out = consulta("clases(L),write(L),nl.")
	return out

def obtenerClasesPorPropiedad(propiedad):
    out = consulta("tiene_propiedad({},Objs),write(Objs),nl.".format(propiedad))
    return out

def obtenerTipo(pokemon):
	out = []
	props = obtenerPropiedades(pokemon)
	props = props[1:-2]
	props = props.split(",")
	for a in props:
		if a[:4] == "tipo":
			out.append(a)
	return out



# todo: Descripcion con la clase
# todo: Obtener todas las clases que cumplen con una propiedad
# Propiedades de los pokemon: tipo,ventaja,color,generacion,no,bipeda

# print(consulta("forall(hombre(X), (write(X),nl))."),end="")
