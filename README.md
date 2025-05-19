
# SmartHome - Proyecto Integrador (Módulo Programador)

Este proyecto simula un sistema básico de gestión de dispositivos inteligentes en un hogar, desarrollado como parte del *ABP del Módulo Programador* del ISPC.

Permite a los usuarios:
- Registrar, listar, buscar y eliminar dispositivos.
- Activar automatizaciones como "Modo Fiesta" y "Modo Noche".



## Funcionalidades

### Gestión de dispositivos

- *Agregar dispositivo*: con nombre, tipo (cámara, luz, música) y estado (encendido/apagado).
- *Listar dispositivos*: muestra todos los dispositivos registrados con sus detalles.
- *Buscar dispositivo*: por nombre, muestra el tipo y estado actual.
- *Eliminar dispositivo*: por nombre.

### Escenarios predefinidos (automatización elegida)

- *Modo Fiesta*:
  - Enciende automáticamente las luces y los equipos de música.
- *Modo Noche*:
  - Apaga las luces y enciende las cámaras de seguridad.



##  Tipos de dispositivos

| Tipo   | Código | Afectado por        |
|--------|--------|---------------------|
| Cámara | 1    | Modo Noche          |
| Luz    | 2    | Modo Fiesta / Noche |
| Música | 3    | Modo Fiesta         |



## Uso del sistema

Al ejecutar el programa (main.py), se accede a un menú de consola:


1. Agregar dispositivo
2. Listar dispositivos
3. Buscar dispositivo
4. Eliminar dispositivo
5. Activar Modo Fiesta
6. Activar Modo Noche
7. Salir



##  Estructura del proyecto

```
abp_programador_ispc/
├── __pycache__/ # Archivos compilados de Python
├── automatizaciones.py # Funciones de escenarios predefinidos
├── dispositivos.py # Funciones de gestión de dispositivos
├── main.py # Menú principal y flujo de usuario
└── README.md # Documentación de este proyecto
```

##  Requisitos técnicos

- Python 3.10 o superior
- Consola o terminal



## 👥Créditos

**Desarrollado por:**
- Sánchez Matías Emanuel  
- Moreira Ignacio Javier  
- Cura Genaro  
- Requelme Kevin Agustín  
- Díaz Esteban Emiliano Gabriel  

**Con la guía de:**
- ROJAS CÓRSICO Ivana Soledad  
- MAINERO Alejandro Luis  
- APERLO Agustina
- OLIVERO José


---

## 🛡️ Política de Protección de Datos para Sistema

- **Tipos de datos personales recolectados:**  
  El sistema puede manejar datos de dispositivos como nombre, tipo y estado. No se almacena información sensible del usuario.

- **Finalidad del procesamiento de datos:**  
  Los datos son utilizados exclusivamente para permitir la automatización del sistema en entornos simulados.

- **Medidas de seguridad implementadas:**  
  El sistema está limitado a ejecución local. No existe comunicación externa ni almacenamiento en la nube, asegurando aislamiento total.

- **Derechos del usuario sobre sus datos:**  
  Los usuarios podrán modificar, eliminar o consultar la información de dispositivos en cualquier momento desde el menú del sistema.

---

## 📜 Plan de Gestión del Trabajo en Equipo

- **Herramientas utilizadas:**  
  GitHub, VS Code, Discord, WhatsApp.

- **Organización y roles asignados:**  
Desde el inicio del proyecto, se optó por una metodología de trabajo colaborativa, donde todos los miembros participaron de manera activa en distintas áreas del desarrollo. La asignación de tareas fue flexible, basada en las fortalezas individuales y en la disponibilidad de cada integrante. Las decisiones clave se tomaban en conjunto, especialmente durante las reuniones por Discord, donde cada uno compartía sus avances y recibía retroalimentación del grupo.
A continuación, se detalla la participación específica de cada integrante:

- Fausto Santino FILI: Contribuyó en la elaboración del Diagrama Entidad-Relación (DER) y fue responsable del desarrollo del apartado de ética dentro del proyecto, además estuvo presente en las llamadas grupales aportando ideas de cómo podrían desarrollar algunas funciones los compañeros de Equipo.

- Matías Emanuel SANCHEZ: Se encargó de implementar la mayoría de las funciones relacionadas con la gestión de dispositivos. Además, trabajó en el desarrollo del inicio del menú principal en el módulo main.py y realizó aportes al archivo README.md del repositorio.

- Kevin Agustín REQUELME: Tuvo a su cargo la implementación y funcionamiento de las opciones del menú desde la opción 1 hasta la opción 4 inclusive. También desarrolló la función eliminar_dispositivo del archivo dispositivos.py y diseño el Diagrama Entidad-Relación según lo establecido en el Grupo.

- Genaro CURA: Fue el principal responsable del documento técnico sobre la base de datos. Asimismo, trabajó de manera conjunta en la función de automatización modo_noche, mostrando una destacada capacidad de colaboración técnica.


Ignacio MOREIRA: Realizó la redacción completa del archivo README.md, habilitó la opción 6 del menú en main.py y contribuyó activamente, junto con Genaro, en la creación de la función de automatización modo_noche.

- Emiliano Gabriel Esteban DIAZ: Habilitó la opción 5 del menú y fue responsable de la función de automatización modo_fiesta. También realizó aportes importantes en el diseño y funcionamiento del menú general.

La participación activa y equilibrada de todos los integrantes garantizó un avance sostenido del proyecto, promoviendo un entorno de respeto y apoyo mutuo.

- **División del trabajo:**  
  El proyecto se dividió en tres módulos principales:  
  1. Gestión de dispositivos  
  2. Automatización de escenarios  
  3. Menú principal y flujo del usuario  

- **Coordinación del trabajo:**  
  Se realizaron reuniones por Discord y seguimiento en WhatsApp.  
  El repositorio en GitHub sirvió para compartir avances y hacer control de versiones.

- **Acuerdos de conducta y compromiso ético:**  
  Se acordó responsabilidad compartida, comunicación clara, y entrega en tiempo y forma como compromiso del equipo.
