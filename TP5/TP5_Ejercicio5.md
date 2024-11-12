**Ejercicio 5: Torneo de ciclismo**

**Esquema de BD:**

'TORNEO <cod_torneo, nombre_torneo, cod_corredor, cod_bicicleta, marca_bicicleta, nyap_corredor, sponsor, DNI_presidente_sponsor, DNI_medico>'

**Restricciones:**

a. El código del torneo es único y no se repite para diferentes torneos. Pero los nombres de torneo pueden repetirse entre diferentes torneos (por ejemplo, el “Tour de Francia” se desarrolla todos los años y siempre lleva el mismo nombre).
b. Un corredor corre varios torneos. Tiene un código único por torneo, pero en diferentes torneos tiene diferentes códigos.
c. Cada corredor tiene varias bicicletas asignadas para un torneo.
d. Los cod_bicicleta pueden cambiar en diferentes torneos, pero dentro de un torneo son únicos.
e. Cada bicicleta tiene una sola marca.
f. Cada corredor tiene varios sponsors en un torneo, y un sponsor puede representar a varios corredores.
g. Cada sponsor tiene un único presidente y un único médico

### Paso 1: Entender las restricciones y dependencias funcionales

- Claves:

    - **cod_torneo** es único para cada torneo, por lo que puede considerarse un candidato a clave para identificar torneos.
    - Cada **cod_corredor** es único en un torneo, pero no entre diferentes torneos.
    - Cada **cod_bicicleta** es único en un torneo, pero puede repetirse en diferentes torneos.
    - Cada **sponsor** tiene un único 'presidente' y 'médico', por lo que hay una dependencia de presidente y médico hacia sponsor.

- Dependencias funcionales:

    - **cod_torneo → nombre_torneo**: el nombre del torneo puede repetirse, pero el código no.
    - **cod_corredor** depende de **cod_torneo** porque es único solo en ese contexto, entonces **(cod_torneo, cod_corredor)** es una clave candidata para los datos del corredor.
    - **cod_bicicleta** también depende del torneo, entonces **(cod_torneo, cod_bicicleta)** es una clave candidata para los datos de la bicicleta.
    - **sponsor → DNI_presidente_sponsor, DNI_medico**: cada sponsor tiene un presidente y médico únicos.

### Paso 2: Primer Forma Normal (1FN)

En 1FN, eliminamos grupos repetitivos y aseguramos que cada atributo tenga solo valores atómicos.

La tabla **TORNEO** ya cumple con la 1FN porque no tiene grupos repetitivos, y cada campo tiene un valor único y atómico.

- Resultado en 1FN:

    - **TORNEO**: (cod_torneo, nombre_torneo, cod_corredor, cod_bicicleta, marca_bicicleta, nyap_corredor, sponsor, DNI_presidente_sponsor, DNI_medico)

### Paso 3: Segunda Forma Normal (2FN)

En 2FN, eliminamos las dependencias parciales, asegurando que cada atributo no clave dependa de toda la clave primaria en las relaciones.

Dado que tenemos dependencias parciales de los atributos en las claves compuestas, debemos descomponer TORNEO en varias tablas.

Descomposición en 2FN:

- **TORNEO**: (cod_torneo, nombre_torneo)
- **CORREDOR_TORNEO**: (cod_torneo, cod_corredor, nyap_corredor, sponsor)
- **BICICLETA_TORNEO**: (cod_torneo, cod_bicicleta, marca_bicicleta)
- **SPONSOR**: (sponsor, DNI_presidente_sponsor, DNI_medico)

Estas tablas eliminan dependencias parciales y cumplen con la 2FN.

### Paso 4: Tercera Forma Normal (3FN)

Para alcanzar la 3FN, eliminamos las dependencias transitivas, de modo que los atributos no clave dependan directamente de la clave primaria.

En las tablas resultantes de 2FN, identificamos las dependencias transitivas:

En 'CORREDOR_TORNEO', el atributo sponsor tiene una dependencia transitiva hacia **DNI_presidente_sponsor** y **DNI_medico** (que están en la tabla 'SPONSOR').

Dado que las dependencias transitivas ya fueron separadas en tablas independientes en 2FN, nuestras relaciones ahora están en 3FN.

- Resultado en 3FN:

    - **TORNEO**: (cod_torneo, nombre_torneo)
    - **CORREDOR_TORNEO**: (cod_torneo, cod_corredor, nyap_corredor, sponsor)
    - **BICICLETA_TORNEO**: (cod_torneo, cod_bicicleta, marca_bicicleta)
    - **SPONSOR**: (sponsor, DNI_presidente_sponsor, DNI_medico)

### Paso 5: Validación de restricciones y ajuste final

Verificamos que las restricciones se respeten en la estructura resultante:

- Cada torneo tiene un **cod_torneo** único en la tabla 'TORNEO'.
- Cada corredor y bicicleta son únicos por torneo en 'CORREDOR_TORNEO' y 'BICICLETA_TORNEO' respectivamente.
- La relación 'SPONSOR' mantiene la unicidad ddel presidente y el médico.

Resumen final de tablas

- **TORNEO**: Almacena datos únicos de cada torneo.
    - Atributos: (cod_tordneo, nombre_torneo)

- **CORREDOR_TORNEO**: Relaciona corredores con torneos y sponsors.
    - Atributos: (cod_torneo, cod_corredor, nyap_corredor, sponsor)

- **BICICLETA_TORNEO**: Relaciona bicicletas con torneos.
    - Atributos: (cod_torneo, cod_bicicleta, marca_bicicleta)

- **SPONSOR**: Almacena la información de cada sponsor, presidente y médico.
    - Atributos: (sponsor, DNI_presidente_sponsor, DNI_medico)

Con esta descomposición, la estructura de la base de datos está en 3FN y cumple con todas las restricciones establecidas.