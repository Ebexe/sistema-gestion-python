# Análisis de Riesgo Crediticio y Gestión de Cartera Morosa

![Status](https://img.shields.io/badge/Status-Completado-success)
![Domain](https://img.shields.io/badge/Domain-Riesgo%20Crediticio-critical)
![Tools](https://img.shields.io/badge/Tools-Python%20%7C%20Power%20BI%20%7C%20Excel-blue)

## Resumen Ejecutivo

Este proyecto simula un **caso real de análisis de riesgo crediticio en banca**, enfocado en la identificación, medición y mitigación de una **exposición de S/ 2.87 millones en cartera morosa**.

El objetivo principal es **transformar datos operativos en decisiones financieras accionables**, integrando:
- **Automatización del scoring crediticio** (Python)
- **Análisis de riesgo y segmentación** (Data Analytics)
- **Visualización ejecutiva para toma de decisiones** (Power BI)

## Objetivo del Proyecto

- Detectar clientes con **alto riesgo de incumplimiento**
- Clasificar automáticamente la cartera crediticia
- Identificar **segmentos con alta exposición financiera**
- Proponer **estrategias de mitigación de riesgo** basadas en datos

## Arquitectura de la Solución

La solución fue diseñada siguiendo principios de **Ingeniería de Software aplicada a analítica financiera**:

### 1. Motor de Reglas de Negocio (Python)
- Implementación de un **algoritmo de scoring crediticio (0–100)**.
- Reglas desacopladas en un módulo independiente (`reglas_negocio.py`).
- Diseño mantenible y escalable para ajustes regulatorios o de política crediticia.

### 2. Pipeline de Datos (ETL)
- Limpieza, transformación y validación de datos crediticios.
- Aplicación automática del score y categorización del riesgo.
- Generación de datasets finales listos para análisis ejecutivo.

### 3. Análisis y Visualización (Power BI)
- Modelado dimensional bajo **Esquema Estrella**.
- KPIs financieros construidos con **DAX**.
- Dashboards orientados a **riesgo, exposición y estrategia**.

## Modelo de Scoring Crediticio

El scoring se basa en reglas de negocio típicas del sector financiero:

- **Estabilidad Laboral:** Penalización a perfiles con ingresos no estables.
- **Tipo de Vivienda:** Ajuste de riesgo según probabilidad de incumplimiento.
- **Finalidad del Crédito:** Penalización a créditos sin retorno económico.

**Resultado:**  
Clasificación automática de clientes en:
- `Normal`
- `Deficiente`

## Principales Hallazgos de Negocio

### Concentración de Riesgo en Vivienda Propia

> El **45% del capital en mora** corresponde a clientes con vivienda propia.

**Interpretación:**  
Aunque el riesgo individual es bajo, el **volumen de capital** genera alta exposición.

**Recomendación:**  
Reforzar políticas de **garantía hipotecaria** y control de concentración.

### Créditos de Consumo no Rentables

- Mora del **84.5%** en créditos destinados a vacaciones.

**Recomendación:**  
Eliminar esta línea de crédito por **riesgo elevado y bajo retorno**.

## Impacto para la Gestión Bancaria

- Mejora en la **detección temprana de riesgo**
- Soporte a decisiones de **política crediticia**
- Identificación de **exposición financiera crítica**
- Base analítica para **comités de riesgo y crédito**

## Estructura del Repositorio

```text
├── data/
│   ├── raw/                      # Datos originales
│   └── processed/                # Datos con score crediticio
├── notebooks/
│   ├── 01_etl_limpieza.ipynb      # Proceso ETL
│   └── 02_eda_visualizacion.ipynb # Análisis exploratorio
├── scripts/
│   └── reglas_negocio.py          # Motor de scoring crediticio
├── dashboard/
│   └── proyecto_credito.pbix      # Dashboard ejecutivo
└── README.md
```


## Tecnologías Utilizadas

- Python: Pandas (procesamiento), lógica de negocio modular.

- Power BI: Modelado dimensional, KPIs financieros, DAX.

- Excel: Fuente de datos operativa.

<div align="center">

Autor:
Eberth Gianfranco Rojas Barbaran

Proyecto orientado a Riesgo Crediticio / Análisis Financiero / Banca

</div> 

<div align="center">

[![Email](https://img.shields.io/badge/Email-Contacto-red?style=for-the-badge&logo=gmail)](mailto:eberthrojas98@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Conectar-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/eberth-gianfranco)

</div>
