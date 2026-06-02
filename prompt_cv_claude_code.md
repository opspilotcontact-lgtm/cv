# PROMPT PARA CLAUDE CODE — CV Juan Ortiz Romero

Necesito que crees un CV profesional en DOS formatos: **HTML interactivo** (que se pueda abrir en navegador y también imprimir como PDF desde el propio navegador) y **PDF generado con Python** (reportlab o weasyprint). Ambos con el mismo contenido pero adaptados a su formato.

## CONTEXTO IMPORTANTE
Este CV es para alguien que se presenta como **desarrollador de software y consultor IA** además de técnico comercial. El diseño del propio CV DEBE demostrar que la persona sabe lo que hace. Si el CV parece genérico o hecho con una plantilla de Canva, contradice el mensaje. Tiene que ser algo que un tech recruiter vea y piense "este tío sabe diseñar y construir cosas".

## DIRECCIÓN ESTÉTICA
- **Tono**: Profesional-técnico pero con personalidad. NO corporativo aburrido, NO "creative agency" exagerado. Piensa en el portfolio de un developer que tiene buen gusto.
- **Layout**: Aprovecha bien el espacio. Puede ser a dos columnas, asimétrico, o con una sidebar. Que respire pero que no desperdicie espacio.
- **Tipografía**: Usa Google Fonts interesantes. Algo como una monospace para labels/categorías (JetBrains Mono, IBM Plex Mono, Space Mono) combinada con una sans moderna para el cuerpo (DM Sans, Outfit, Satoshi si está disponible, Manrope). NO uses Inter, Roboto, Arial.
- **Color**: Paleta contenida y sofisticada. Un fondo oscuro para el header (tipo slate/charcoal #1a1a2e), un accent verde bosque (#2d5a27) para puntos de atención, el resto limpio. Puede haber toques sutiles como un noise texture o un gradiente muy sutil.
- **Detalles que marquen diferencia**: 
  - Micro-animaciones sutiles en hover para la versión HTML (links, skill tags)
  - Los links de prensa deben ser clicables y verse profesionales
  - Un badge/chip visual para "Finalista EmprendeUCO 2025" que llame la atención
  - Las skill tags con un estilo tipo "tech stack" que cualquier developer reconocería
  - Print styles en el HTML para que al imprimir quede perfecto (sin fondos problemáticos, con URLs visibles)
- **Responsive**: El HTML debe verse bien en móvil también.
- **NO quiero**: Foto de perfil, iconos de FontAwesome genéricos, bordes redondeados exagerados, gradientes rainbow, nada que parezca template de Canva/Figma gratuito.

## CONTENIDO EXACTO DEL CV

### CABECERA
- **Nombre**: Juan Ortiz Romero
- **Titular**: Técnico Comercial · Desarrollo Software · IA
- **Teléfono**: 605 098 187
- **Email**: Juanortiz11615@gmail.com
- **Ubicación**: Córdoba, España

### PERFIL
Profesional con formación en comercio internacional y experiencia en venta consultiva en el sector de construcción y reformas. Desarrollo software como actividad propia, combinando habilidades técnicas (React, TypeScript, Supabase) con visión de negocio. Fundador de OpsPilot, proyecto finalista en el programa EmprendeUCO – Diputación de Córdoba 2024-2025. Busco oportunidades donde conectar capacidad comercial con desarrollo web y aplicación de inteligencia artificial.

### EXPERIENCIA LABORAL

**Vendedor Especialista — Obramat**
jun 2025 — actualidad · Córdoba · Sector construcción y reformas
- Elaboración de presupuestos técnicos para profesionales y particulares.
- Gestión de stock, reposición y control de inventario en sección.
- Venta consultiva y asesoramiento técnico al cliente.
- Seguimiento de pedidos y coordinación con almacén.

**Prácticas Académicas — El Corte Inglés**
mar 2023 — jun 2023 · Córdoba
- Atención al cliente y venta directa.
- Reposición y almacenaje de mercancía.
- Cobro y gestión de caja.

### PROYECTOS PROPIOS

**OpsPilot** [DESTACAR VISUALMENTE COMO BLOQUE PRINCIPAL]
Badge: "Finalista EmprendeUCO 2025"
Descripción: Plataforma SaaS de gestión empresarial desarrollada íntegramente de forma autónoma. Centraliza presupuestos, inventario y operaciones en un solo sistema, orientada a autónomos y pequeñas empresas del sector construcción y reformas. Stack técnico: React, TypeScript, Supabase (PostgreSQL + Row Level Security), Vercel. Seleccionado entre los 20 proyectos finalistas (de 60 presentados) en el programa EmprendeUCO – Diputación de Córdoba 2024-2025.

Links de prensa verificables (DEBEN ser clicables en ambos formatos):
- EmprendeUCO Portfolio: https://emprendeuco.es/portfolio/opspilot/
- Cordópolis (elDiario.es): https://cordopolis.eldiario.es/universidad/semillas-emprendimiento-plantadas-mano-universidad-cordoba-diputacion_1_12391407.html
- CordobaBN: https://www.cordobabn.com/articulo/educacion/emprendeuco-diputacion-presenta-20-ideas-negocio-fase-final/20250617123851228107.html
- Fundecor: https://fundecor.es/2025/06/17/emprendeuco-diputacion-de-cordoba-presenta-las-20-ideas-de-negocio-que-compiten-en-su-fase-final/

### FORMACIÓN ACADÉMICA
- **CFGS Comercio Internacional** — IES Luis de Góngora, Córdoba (2023–2025)
- **CFGM Actividades Comerciales** — CES Ramón y Cajal, Córdoba (2021–2023)
- **ESO** — IES El Sauce, La Carlota, Córdoba (2016–2020)

### FORMACIÓN COMPLEMENTARIA
**Programa EmprendeUCO — Diputación de Córdoba** (2024–2025)
Universidad de Córdoba · +120 horas
- Formación intensiva en emprendimiento: modelo de negocio, validación, propuesta de valor.
- Mentorías especializadas, asesoramiento estratégico y planificación financiera.
- IA aplicada al negocio, marketing digital y escalado empresarial.

### HABILIDADES TÉCNICAS
Organizadas en 4 categorías visuales:

**Desarrollo**: React · TypeScript · Vite · HTML/CSS · JavaScript
**Backend & Datos**: Supabase · PostgreSQL · Row Level Security · APIs REST
**Infraestructura**: Vercel · VPS · Git · Cloudflare
**IA & Herramientas**: Desarrollo asistido por IA · Prompting avanzado · Claude / LLMs

### INFORMACIÓN ADICIONAL
- **Idiomas**: Español (nativo) · Inglés (nivel alto)
- **Disponibilidad**: Total
- **Movilidad**: Carnet de conducir + coche propio
- **Nacimiento**: 26 de agosto de 2004 · Córdoba

### PIE
"Juan Ortiz Romero — Actualizado junio 2026"

## ENTREGABLES
1. **cv_juan_ortiz.html** → HTML completo, standalone (CSS inline o en <style>, Google Fonts via link), con hover effects, links clicables, responsive, y print-ready (@media print).
2. **cv_juan_ortiz.pdf** → PDF generado con Python, una sola página A4, mismo contenido, links clicables, diseño limpio y profesional.

Ambos archivos en /mnt/user-data/outputs/

## NOTA FINAL
Lee las skills de frontend-design y pdf ANTES de escribir código. El nivel de calidad debe ser el de alguien que dice dedicarse a esto profesionalmente. Si el CV no impresiona visualmente, el contenido pierde credibilidad.
