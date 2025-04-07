
# INSTRUCTIONS MMM

## Índice

1. Tabla para MMM: Sales
   - 1.1 Tabla INV (Inversión en publicidad)
   - 1.2 Tabla WEB (Tráfico e interacciones online)
   - 1.3 Tabla OFFLINE (Datos de tienda física)
   - 1.4 Tabla TIME (Factores temporales)
   - 1.5 Tabla VISIT (Visitas web por categoría)
   - 1.6 Columnas creadas (retardos)



## 1. Tabla para MMM: Sales

El modelo de atribución tiene como objetivo explicar las ventas físicas (`Sales_off`) a partir de múltiples variables recogidas en distintas tablas. A continuación, se listan y describen brevemente todas las columnas del DataFrame `df_merge`, organizadas por su origen.

### 1.1 Tabla INV (Inversión en publicidad)

| Columna            | Descripción breve                          |
|--------------------|---------------------------------------------|
| CINE               | Inversión en cine                           |
| EXTERIOR           | Inversión en publicidad exterior            |
| INTERNET           | Inversión en internet                       |
| PRENSA             | Inversión en prensa                         |
| PRODUCCION         | Costes de producción de marketing           |
| RADIO              | Inversión en radio                          |
| REVISTAS           | Inversión en revistas                       |
| PlataformasVideo   | Inversión en plataformas de video           |
| VARIOS             | Otros gastos de marketing                   |
| INV_Total          | Inversión total                             |
| Pct_Online         | Porcentaje de inversión en medios online    |
| Pct_Offline        | Porcentaje de inversión en medios offline   |

### 1.2 Tabla WEB (Tráfico e interacciones online)

| Columna                      | Descripción breve                          |
|------------------------------|---------------------------------------------|
| Unique_visitors              | Visitantes únicos a la web                 |
| PDFBrochuresDownloaded       | Número de catálogos PDF descargados        |
| ProductConfigurator          | Veces que se usó el configurador           |
| Product_configurator_Visists | Visitas al configurador                    |
| SocialNetworks               | Tráfico web desde redes sociales           |
| DirectTraffic                | Tráfico directo a la web                   |
| EMail                        | Tráfico desde campañas de correo           |
| NaturalSearch                | Tráfico desde búsquedas orgánicas          |
| OnlineMedia                  | Tráfico desde medios online                |
| OtherReferrer                | Tráfico desde otras fuentes                |
| PaidSearch                   | Tráfico desde anuncios en buscadores       |

### 1.3 Tabla OFFLINE (Datos de tienda física)

| Columna            | Descripción breve                          |
|--------------------|---------------------------------------------|
| Visit_Store_off    | Visitas a tienda física                    |
| Mercado_off        | Demanda en tienda                          |
| Sales_off          | Ventas físicas                             |
| Complementos_off   | Ventas en complementos                     |
| Ropa_hombre_off    | Ventas ropa de hombre                      |
| Zapatos_off        | Ventas de zapatos                          |
| Ropa_Mujer_off     | Ventas ropa de mujer                       |
| Home_off           | Ventas de productos de hogar               |
| Interior_off       | Ventas ropa interior                       |
| Otros_off          | Ventas de otros productos                  |
| Ticket_medio_off   | Valor medio de cada compra                 |

### 1.4 Tabla TIME (Factores temporales)

| Columna            | Descripción breve                          |
|--------------------|---------------------------------------------|
| Dias_mes           | Total días del mes                         |
| Dia_inicio_mes     | Día de inicio del mes                      |
| Dia_findemes       | Día de fin de mes                          |
| working_days       | Número de días laborables del mes          |
| Dias_fines_semana  | Número de fines de semana del mes          |
| Easterweek         | Indicador de Semana Santa                  |

### 1.5 Tabla VISIT (Visitas web por categoría)

| Columna            | Descripción breve                          |
|--------------------|---------------------------------------------|
| RopaHombre_visit   | Visitas a ropa de hombre                   |
| RopaMujer_visit    | Visitas a ropa de mujer                    |
| Complementos_visit | Visitas a complementos                    |
| Zapatos_visit      | Visitas a zapatos                         |
| Home_visit         | Visitas a productos de hogar              |
| Interior_visit     | Visitas a ropa interior                   |
| Otros_visit        | Visitas a otros productos                 |
| SR_Total_visit     | Suma total de visitas por categoría       |

### 1.6 Columnas creadas (retardos)

| Columna         | Descripción breve                           |
|------------------|----------------------------------------------|
| Sales_1_ago      | Ventas físicas del mes anterior              |
| Sales_2_ago      | Ventas físicas de hace dos meses             |
