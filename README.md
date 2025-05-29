# G13_Comision_1

"Breve descripción del trabajo"
Simulador de logística para el INCUCAI: Este proyecto modela un sistema de gestión de trasplantes de órganos en Argentina, incluyendo la asignación de órganos, disponibilidad de cirujanos, transporte y centros de salud. Permite simular distintos escenarios de donación y recepción, priorizando criterios médicos y logísticos.
---

## Integrantes

* **Docentes:**
    * Fernando Romero Muñoz
    * Camila Zavidowski
* **Alumnos:**
    * Hipólito Giménez
    * Trinidad Bayerque

---

## Objetivo del proyecto

_**Nota:** Este proyecto se enfoca en la gestión de donantes y receptores de órganos, simulando un sistema de gestión para INCUCAI._

---

## Configuración y Ejecución

Para ejecutar este proyecto, asegúrate de tener Python 3.x instalado (se recomienda usar un entorno virtual como Anaconda para manejar las dependencias).


1.  **Clonar el repositorio:**
    ```bash
    https://github.com/HipolitoGimenez/TP-LP1--G13-Gimenez-Bayerque.git
    ```

2.  **Configurar el entorno (Opcional, pero recomendado):**
    Si usas Anaconda, puedes crear un entorno virtual:
    ```bash
    conda create -n mi_entorno_tp_lp1 python=3.10 # O la versión de Python que uses
    conda activate mi_entorno_tp_lp1
    ```
    Si usas `venv`:
    ```bash
    python -m venv venv
    .\venv\Scripts\activate # En Windows PowerShell
    # source venv/bin/activate # En Linux/macOS
    ```

3.  **Diagrama UML:**
    Puedes ver el diagrama UML del proyecto aquí:
    [Diagrama UML del Proyecto](https://app.diagrams.net/#G1wymQ_Uzuawb6E07xZvPAKNnipn-7bt_2#%7B%22pageId%22%3A%22gMXmehYRXr0v4xTKnlDv%22%7D)

4.  **Ejecutar el programa principal:**
    Desde la raíz del proyecto (`TP-LP1`), ejecuta el archivo `main.py`:
    ```bash
    python main.py
    ```

---

## Estructura del Proyecto

El proyecto está organizado en módulos dentro de la carpeta `src` para una mejor modularización, el cual consta de 4 carpetas principales:

* **`Vehiculos/`**: Contiene las clases `vehiculos`, `auto`, `avion` y `helicoptero`.
* **`Sistema/`**: Contiene la clase `INCUCAI`.
* **`Personas/`**: Contiene las clases `cirujano`, `paciente`, `receptor` y `donantes`.
* **`Modelos/`**: Contiene las clases `centro de salud`, `viaje`, `organo` y `tipoOrganoEnum`.

---

## Licencia

Este proyecto está bajo la Licencia Pública General GNU v3.0 (GPL-3.0).

---
