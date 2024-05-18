%REGLAS DE INFERENCIA
subc(C1,C2):- frame(C1,subclase_de(C2),_,_).
subc(C1,C2):- frame(C1,subclase_de(C3),_,_),subc(C3,C2).
subclase(X):-frame(X,subclase_de(_),_,_).

%Para consultar propiedades use: propiedadesc(luciernaga, L).
propiedadesc(top,_):-!.
propiedadesc(X,Z):-frame(X,subclase_de(Y),propiedades(P),descripcion(_)),propiedadesc(Y,P1), concatenar(P1,P,W),de_reversa(W,Z).


%Para consultar todas las clases representadas en los frames
clases(L):-findall(X,frame(X,subclase_de(_),propiedades(_),descripcion(_)),L).

%Para consultar todas las subclases de una una clase
subclases_de(X,L):-findall(C1,subc(C1,X),L).

%Para consultar todas las superclases de una clase
superclases_de(X,L):-findall(C1,subc(X,C1),S),de_reversa(S,L).

%Para consultar qué objetos tienen UNA propiedad determinada
tiene_propiedad(P,Objs):-frame(X,_,propiedades(L),descripcion(_)),member(P,L),subclases_de(X,S),select(X,Objs,S),!.

%Obtiene todas las propiedades de todos los objetos
todas_propiedades(L):-findall(P,frame(_,_,propiedades(P),descripcion(_)),NL), flatten(NL,L).

%Obtiene la descripcion de un clase

obtiene_descripcion(C,D):-frame(C,_,_,descripcion(D)).

% Obtiene una lista de clases con los objetos que tienen la propiedades
% de la lista de entrada en P
consulta_por_propiedades(P,C):-consulta(P,C1),list_to_set(C1,C2),sort(C2,C).

consulta([],[]).
consulta([H|T],C):-consulta(T,C1), tiene_propiedad(H,C2),append(C1,C2,C).

%Es hoja (regresa verdadero si la clase no tiene subclases)
%
es_hoja(Clase):-subclases_de(Clase,L),L = [].


%Unir dos listas en una tercera
concatenar([],L,L).
concatenar([X|L1],L2,[X|L3]):-concatenar(L1,L2,L3).

% Agregar un elemento al final de una lista
% ?- agregar_final([a,b],c,L).
agregar_final([],E,[E]).
agregar_final([C|R],E,[C|RL]) :- agregar_final(R,E,RL).

%  Invertir una lista
%  ?-de_reversa([1,2,3],L).
de_reversa([X],[X]).
de_reversa([C|R],L) :- de_reversa(R,RI), agregar_final(RI,C,L).

%BASE DE CONOCIMIENTOS

% ventaja de tipos

ventaja(fuego,planta).
ventaja(fuego,hielo).
ventaja(fuego,bicho).
ventaja(agua,fuego).
ventaja(agua,tierra).
ventaja(agua,roca).
ventaja(electrico,agua).
ventaja(electrico,volador).
ventaja(planta,agua).
ventaja(planta,tierra).
ventaja(planta,roca).
ventaja(hielo,planta).
ventaja(hielo,tierra).
ventaja(hielo,volador).
ventaja(hielo,dragon).
ventaja(lucha,normal).
ventaja(lucha,hielo).
ventaja(lucha,roca).
ventaja(veneno,planta).
ventaja(veneno,bicho).
ventaja(tierra,fuego).
ventaja(tierra,electrico).
ventaja(tierra,veneno).
ventaja(tierra,roca).


% pokemones

% test:- once((propiedadesc(bulbasaur, L),write(L),nl)).

frame(pokemon,subclase_de(top),
      propiedades([necesita(respirar)]),
      descripcion('Pokemon son criaturas miticas que pueden ser atrapados con Pokeballs.')).

% frame(nombre,subclase_de(pokemon),
%       propiedades([]),
%       descripcion('')).

frame(bulbasaur,subclase_de(pokemon),
      propiedades([tipo(planta),tipo(veneno),color(verde),generacion(1),no('0001'),tiene(cuatro_patas)]),
      descripcion('pokemon tipo planta con la que puedes iniciar el juego.')).

frame(ivysaur,subclase_de(bulbasaur),
      propiedades([tipo(planta),tipo(veneno),color(verde),generacion(1),no('0002'),tiene(cuatro_patas)]),
      descripcion('evolucion de balbasaur.')).

frame(venusaur,subclase_de(ivysaur),
      propiedades([tipo(planta),tipo(veneno),color(verde),generacion(1),no('0003'),tiene(cuatro_patas)]),
      descripcion('evolucion de venusaur.')).

frame(charmander,subclase_de(pokemon),
      propiedades([tipo(fuego),color(rojo),generacion(1),no('0004'),tiene(dos_patas)]),
      descripcion('pokemon tipo fuego con la que puedes iniciar el juego.')).

frame(charmeleon,subclase_de(charmander),
      propiedades([tipo(fuego),color(rojo),generacion(1),no('0005'),tiene(dos_patas)]),
      descripcion('evolucion de charmander.')).

frame(charizard,subclase_de(charmeleon),
    propiedades([tipo(fuego),tipo(volador),color(rojo),generacion(1),no('0006'),tiene(dos_patas)]),
    descripcion('evolucion de charmeleon.')).

frame(squirtle,subclase_de(pokemon),
	propiedades([tipo(agua),color(azul),generacion(1),no('0007'),tiene(dos_patas)]),
	descripcion('pokemon tipo agua con la que puedes iniciar el juego.')).

frame(wartortle,subclase_de(squirtle),
	propiedades([tipo(agua),color(azul),generacion(1),no('0008'),tiene(dos_patas)]),
	descripcion('evolucion de squirtle.')).

frame(blastoise,subclase_de(wartortle),
	propiedades([tipo(agua),color(azul),generacion(1),no('0009'),tiene(dos_patas)]),
	descripcion('evolucion de wartortle.')).

frame(pikachu,subclase_de(pokemon),
      propiedades([tipo(electrico),color(amarillo),generacion(1),no('0025'),tiene(dos_patas)]),
      descripcion('pokemon electrico con la aparencia de una ardilla amarilla.')).

frame(raichu,subclase_de(pikachu),
      propiedades([tipo(electrico),color(amarillo),generacion(1),no('0026'),tiene(dos_patas)]),
      descripcion('evolucion de pikachu.')).

frame(ekans,subclase_de(pokemon),
      propiedades([tipo(veneno),color(morado),generacion(1),no('0023'),tiene(cero_patas)]),
      descripcion('pokemon morado que se parece a un serpiente.')).

frame(arbok,subclase_de(ekans),
      propiedades([tipo(veneno),color(morado),generacion(1),no('0024'),tiene(cero_patas)]),
      descripcion('evolucion de ekans.')).

frame(ditto,subclase_de(pokemon),
      propiedades([tipo(normal),color(morado),generacion(1),no('0132'),tiene(cero_patas)]),
      descripcion('pokemon que puede imitar la aparencia de cualqueir otro pokemon.')).

frame(eevee,subclase_de(pokemon),
      propiedades([tipo(normal),color(cafe),generacion(1),no('0133'),tiene(cuatro_patas)]),
      descripcion('pokemon que tiene muchas evoluciones y tiene 
      caracteristicas similares a aquellos de zorros y perros.')).


frame(vaporeon,subclase_de(eevee),
      propiedades([tipo(agua),color(azul),generacion(1),no('0134'),tiene(cuatro_patas)]),
      descripcion('un posible camino de evolucion de eevee.')).

frame(jolteon,subclase_de(eevee),
	propiedades([tipo(agua),color(azul),generacion(1),no('0135'),tiene(cuatro_patas)]),
	descripcion('un posible camino de evolucion de eevee.')).

frame(flareon,subclase_de(eevee),
	propiedades([tipo(fuego),color(rojo),generacion(1),no('0136'),tiene(cuatro_patas)]),
	descripcion('un posible camino de evolucion de eevee.')).

frame(voltorb,subclase_de(pokemon),
      propiedades([tipo(electrico), color(rojo),color(blanco),generacion(1),no('0100'),tiene(cero_patas)]),
      descripcion('tiene la aparencia de una pokebola y se puede autodestruir.')).

frame(pidgey,subclase_de(pokemon),
      propiedades([tipo(volador), tipo(normal),color(cafe),generacion(1),no('0016'),tiene(dos_patas)]),
      descripcion('un pajaro.')).
      
% Pokémon de tipo Lucha
frame(machop, subclase_de(pokemon),
      propiedades([tipo(lucha), color(gris), generacion(1), no('0066'), tiene(dos_patas)]),
      descripcion('un pequeño Pokémon luchador conocido por su fuerza física.')).
frame(machoke, subclase_de(machop),
      propiedades([tipo(lucha), color(gris), generacion(1), no('0067'), tiene(dos_patas)]),
      descripcion('la evolución de Machop, más fuerte 
      y más definido muscularmente.')).
frame(machamp, subclase_de(machoke),
      propiedades([tipo(lucha), color(gris), generacion(1), no('0068'), tiene(dos_patas)]),
      descripcion('la forma final de Machop, conocido 
      por sus cuatro brazos poderosos.')).

% Pokémon de tipo Siniestro
frame(umbreon, subclase_de(eevee),
      propiedades([tipo(siniestro), color(negro), generacion(2), no('0197'), tiene(cuatro_patas)]),
      descripcion('una evolución de Eevee que se manifiesta cuando se expone a energías oscuras.')).
      
% Pokémon de tipo Hada
frame(sylveon, subclase_de(eevee),
      propiedades([tipo(hada), color(rosa), generacion(6), no('0700'), tiene(cuatro_patas)]),
      descripcion('una evolución de Eevee que puede manifestarse 
      cuando se tiene un gran vínculo afectivo.')).

      
% Pokémon de tipo Psíquico
frame(espeon, subclase_de(eevee),
      propiedades([tipo(psiquico), color(lila), generacion(2), no('0196'), tiene(cuatro_patas)]),
      descripcion('una evolución de Eevee que se desarrolla cuando 
      hay un fuerte vínculo psíquico con su entrenador.')).
frame(alakazam, subclase_de(pokemon),
      propiedades([tipo(psiquico), color(cafe), generacion(1), no('0065'), tiene(dos_patas)]),
      descripcion('un Pokémon con habilidades psíquicas excepcionales y una inteligencia sobrehumana.')).

      
% Pokémon de tipo Roca

frame(geodude, subclase_de(pokemon),
      propiedades([tipo(roca),color(gris), generacion(1), no('0074'), tiene(dos_patas)]),
      descripcion('un Pokémon roca que comúnmente se encuentra en caminos montañosos.')).
      
% Pokémon de tipo Tierra
frame(diglett, subclase_de(pokemon),
      propiedades([tipo(tierra), color(cafe), generacion(1), no('0050'), tiene(cero_patas)]),
      descripcion('un Pokémon de tipo tierra que vive bajo tierra, emergiendo solo su cabeza.')).

