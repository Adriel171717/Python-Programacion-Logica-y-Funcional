% humedad()
% temperatura(36)
% hora_adecuada()
% probabilidad_lluvia()
% recomendaciones :-

% 1 el sistema considera que la hora es adecuada para regar si es antes de las 10 am
% 2 el riego se activa automaticamente si:
%    --la humedad de suelo es baja
%    --No se pronostica lluvia
%    --Y es una hora adecuada para regar
% 3 si el riego esta activado, se registra el estado como "Activado"; si no, como "No activado"

% 4 Alerta por condiciones extremas
% si la temperatura es mayor o igual a 32°C, se activa una alerta por calor extremo
% Si el riego se activa bajo esas condiciones, el sistema emite una recomendacion:
% "Alerta: Riego activado con temperatura alta. Considere riego nocturno o por goteo."

% 5 En caso contrario, indica:
% "Sin recomendaciones especiales para el riego."

% ------------------------------------------------------------------------------------------------

% ------------------Base de conocimiento por zona ------------------


% Formato: zona(NombreZona, Humedad, Temperatura, Hora, Lluvia).
zona(norte, baja, 36, 4, false).
zona(sur, media, 33, 18, true).
zona(este, baja, 34, 8, false).
zona(oeste, alta, 28, 10, true).


% ------------------ Reglas generales ------------------

% 1. Hora adecuada para riego: antes de las 10 am o después de las 6 pm
hora_adecuada(Hora) :-
    Hora < 10 ;
    Hora > 18.

% 2. Activar riego si: humedad baja, no hay lluvia, y hora adecuada
activar_riego(Humedad, Lluvia, Hora) :-
    Humedad = baja,
    Lluvia = false,
    hora_adecuada(Hora).

% 3. Diagnóstico del sistema de riego por zona
estado_riego(Zona, 'Activado') :-
    zona(Zona, Humedad, _, Hora, Lluvia),
    activar_riego(Humedad, Lluvia, Hora).

estado_riego(Zona, 'No activado') :-
    zona(Zona, Humedad, _, Hora, Lluvia),
    \+ activar_riego(Humedad, Lluvia, Hora).

% 4. Alerta por calor extremo si temperatura ≥ 32
alerta_calor(Temp) :-
    Temp >= 32.

% 5. Recomendaciones por zona
recomendacion(Zona) :-
    zona(Zona, Humedad, Temp, Hora, Lluvia),
    activar_riego(Humedad, Lluvia, Hora),
    alerta_calor(Temp),
    !,
    format('Zona ~w: Alerta: Riego activado con temperatura alta (~w°C). Considere riego nocturno o por goteo.~n', [Zona, Temp]).

recomendacion(Zona) :-
    zona(Zona, Humedad, Temp, Hora, Lluvia),
    activar_riego(Humedad, Lluvia, Hora),
    !,
    format('Zona ~w: Riego activado. Sin recomendaciones especiales.~n', [Zona]).

recomendacion(Zona) :-
    format('Zona ~w: Riego no activado. No se cumplen las condiciones necesarias.~n', [Zona]).


% ------------------ Consulta principal para todas las zonas ------------------

reporte_general :-
    findall(Z, zona(Z, _, _, _, _), Zonas),
    forall(member(Zona, Zonas), (
        estado_riego(Zona, Estado),
        format('Zona ~w: Estado del riego: ~w~n', [Zona, Estado]),
        recomendacion(Zona),
        writeln('---')
    )).
