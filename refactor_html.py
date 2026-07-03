import os

def refactor_html():
    html_path = r"c:\Users\YASITCOMPUTER\Documents\Anty Proyectos\pagina web Necsa\index.html"
    
    if not os.path.exists(html_path):
        print(f"File not found: {html_path}")
        return

    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Define the search and replace patterns in order
    replacements = []

    # 1. Header Logo
    search_1 = """      <!-- Logotipo Oficial Integrado de Necsa -->
      <a href="#inicio" class="logo" id="logo-link">
        <img src="assets/images/logo-nuevo.png" alt="Logo Necsa Constructora" class="logo-img">
      </a>"""
    
    replace_1 = """      <!-- Logotipo Oficial Integrado de Necsa -->
      <a href="#inicio" class="logo" id="logo-link">
        <img src="assets/images/logo%201%20con%20texto.png" alt="Logo Necsa Constructora" class="logo-img">
      </a>"""
    
    replacements.append((search_1, replace_1))

    # 2. Hero Section
    search_2 = """  <!-- --- HERO SECTION --- -->
  <section class="hero" id="inicio">
    <div class="hero-bg">
      <img src="assets/images/hero-obra.png" alt="Obras Civiles Necsa en Santiago de Chile">
    </div>
    <div class="container hero-container">
      <div class="hero-content">
        <div class="hero-company">NECSA <span style="font-weight: 300; color: var(--color-secondary-light);">CONSTRUCTORA</span></div>
        <div class="hero-badge">
          <i class="fa-solid fa-helmet-safety"></i> Edificación y Estructuras en Santiago de Chile
        </div>
        <h1 class="hero-title">Ingeniería y Construcción de <span>Vanguardia</span></h1>
        <p class="hero-description">En Necsa somos líderes en la ejecución de desarrollos residenciales premium y obras comerciales de alta complejidad estructural. Cumplimiento absoluto de la normativa OGUC y estándares sismorresistentes.</p>
        <div class="hero-actions">
          <a href="#proyectos" class="btn btn-accent"><i class="fa-solid fa-compass-drafting"></i> Ver Obras Realizadas</a>
      </div>
    </div>
  </section>"""

    replace_2 = """  <!-- --- HERO SECTION --- -->
  <section class="hero" id="inicio">
    <div class="hero-bg">
      <img src="assets/images/hero-obra.png" alt="Obras Civiles Necsa en Santiago de Chile">
    </div>
    <div class="container hero-container">
      <div class="hero-content">
        <div class="hero-company">NECSA <span style="font-weight: 300; color: var(--color-secondary-light);">CONSTRUCTORA</span></div>
        <h1 class="hero-title">Ingeniería y Construcción de <span>Vanguardia</span></h1>
        <p class="hero-tagline">“Construimos con visión, ejecutamos con excelencia”</p>
        <p class="hero-description">En NECSA construimos y desarrollamos proyectos con visión, eficiencia y excelencia técnica, buscando soluciones constructivas confiables e innovadoras, priorizando la seguridad, la calidad y el cumplimiento, bajo una filosofía basada en el buen construir, la lealtad y compromiso total con nuestros clientes.</p>
        <div class="hero-actions">
          <a href="#proyectos" class="btn btn-accent"><i class="fa-solid fa-compass-drafting"></i> Ver Obras Realizadas</a>
        </div>
      </div>
    </div>
  </section>"""
    
    replacements.append((search_2, replace_2))

    # 3. Nosotros Section
    search_3 = """  <!-- --- SECCIÓN NOSOTROS --- -->
  <section class="section" id="nosotros">
    <div class="container">
      <div class="about-wrapper" style="max-width: 900px; margin: 0 auto; text-align: center; margin-bottom: var(--spacing-lg);">
        <h2 class="section-title" style="display: block; margin-bottom: var(--spacing-md);">Solidez, Rigor Técnico y Confianza</h2>
        <p class="contact-lead" style="margin-bottom: var(--spacing-sm); font-size: 1.25rem;">Edificamos con los más altos estándares de calidad estructural y terminaciones arquitectónicas en toda la Región Metropolitana.</p>
        <p style="color: var(--text-muted); margin-bottom: var(--spacing-lg); font-size: 1.05rem; line-height: 1.8;">
          Necsa Constructora se destaca por ofrecer soluciones constructivas integrales que combinan la robustez de la ingeniería de acero e infraestructura con la sofisticación de la arquitectura moderna. Nuestro equipo multidisciplinario asegura procesos seguros, eficientes y alineados estrictamente con el marco regulatorio chileno (OGUC y normas sísmicas de cálculo NCh433).
        </p>
      </div>
      
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: var(--spacing-md); max-width: 1000px; margin: 0 auto;">
        <!-- Card Misión -->
        <div style="padding: var(--spacing-lg); border-top: 4px solid var(--color-primary); background-color: var(--bg-secondary); border-radius: var(--border-radius-md); box-shadow: var(--shadow-sm); display: flex; flex-direction: column; gap: var(--spacing-sm);">
          <div style="width: 50px; height: 50px; background-color: var(--color-primary-light); color: var(--color-primary); border-radius: var(--border-radius-sm); display: flex; align-items: center; justify-content: center; font-size: 1.5rem;">
            <i class="fa-solid fa-bullseye"></i>
          </div>
          <h3 style="font-family: var(--font-headings); font-size: 1.5rem; color: var(--color-primary); margin: 0;">Misión</h3>
          <p style="font-size: 1rem; color: var(--text-dark); line-height: 1.7; text-align: justify; margin: 0;">
            En NECSA construimos y desarrollamos proyectos con visión, eficiencia y excelencia técnica, buscando soluciones constructivas confiables e innovadoras, priorizando la seguridad, la calidad y el cumplimiento, bajo una filosofía basada en el buen construir, la lealtad y compromiso total con nuestros clientes.
          </p>
        </div>
        
        <!-- Card Visión -->
        <div style="padding: var(--spacing-lg); border-top: 4px solid var(--color-accent); background-color: var(--bg-secondary); border-radius: var(--border-radius-md); box-shadow: var(--shadow-sm); display: flex; flex-direction: column; gap: var(--spacing-sm);">
          <div style="width: 50px; height: 50px; background-color: var(--color-accent-light); color: var(--color-accent); border-radius: var(--border-radius-sm); display: flex; align-items: center; justify-content: center; font-size: 1.5rem;">
            <i class="fa-solid fa-eye"></i>
          </div>
          <h3 style="font-family: var(--font-headings); font-size: 1.5rem; color: var(--color-primary); margin: 0;">Visión</h3>
          <p style="font-size: 1rem; color: var(--text-dark); line-height: 1.7; text-align: justify; margin: 0;">
            Queremos ser una empresa referente en construcción e infraestructura a nivel nacional, reconocida por su capacidad de ejecución, innovación, confiabilidad y excelencia operacional, aportando valor sostenible en cada proyecto que desarrollamos.
          </p>
        </div>
      </div>
    </div>
  </section>"""

    replace_3 = """  <!-- --- SECCIÓN NOSOTROS --- -->
  <section class="section" id="nosotros">
    <div class="container">
      <div class="about-wrapper" style="max-width: 900px; margin: 0 auto; text-align: center; margin-bottom: var(--spacing-lg);">
        <h2 class="section-title" style="display: block; margin-bottom: var(--spacing-md);">Solidez, Rigor Técnico y Confianza</h2>
      </div>
      
      <div class="vision-container" style="max-width: 800px; margin: 0 auto;">
        <!-- Card Visión -->
        <div class="vision-card" style="padding: var(--spacing-lg); border-left: 5px solid var(--color-accent); background-color: var(--bg-secondary); border-radius: var(--border-radius-md); box-shadow: var(--shadow-md); display: flex; flex-direction: column; gap: var(--spacing-sm);">
          <div style="width: 50px; height: 50px; background-color: var(--color-accent-light); color: var(--color-accent); border-radius: var(--border-radius-sm); display: flex; align-items: center; justify-content: center; font-size: 1.5rem;">
            <i class="fa-solid fa-eye"></i>
          </div>
          <h3 style="font-family: var(--font-headings); font-size: 1.75rem; color: var(--color-primary); margin: 0;">Nuestra Visión</h3>
          <p style="font-size: 1.15rem; color: var(--text-dark); line-height: 1.8; text-align: justify; margin: 0;">
            Queremos ser una empresa referente en construcción e infraestructura a nivel nacional, reconocida por su capacidad de ejecución, innovación, confiabilidad y excelencia operacional, aportando valor sostenible en cada proyecto que desarrollamos.
          </p>
        </div>
      </div>
    </div>
  </section>"""

    replacements.append((search_3, replace_3))

    # 4. Portafolio Section
    search_4 = """  <!-- --- SECCIÓN PORTAFOLIO (PROYECTOS) --- -->
  <section class="section" id="proyectos">
    <div class="container">
      <div class="section-title-wrapper">
        <h2 class="section-title">Nuestras Obras Destacadas</h2>
        <p class="section-subtitle">Conoce nuestros principales proyectos ejecutados con éxito en la Región Metropolitana, evidenciando excelencia y solidez constructiva.</p>
      </div>
      
      <!-- Filtros del Portafolio -->
      <div class="portfolio-filters">
        <button class="filter-btn active" data-filter="all">Todos los Proyectos</button>
        <button class="filter-btn" data-filter="residenciales">Residenciales Premium</button>
        <button class="filter-btn" data-filter="comerciales">Comerciales e Industriales</button>
      </div>
      
      <!-- Grid de Proyectos -->
      <div class="portfolio-grid">
        
        <!-- Proyecto 1: Plaza Blest (Comercial) -->
        <div class="portfolio-item" data-category="comerciales">
          <img src="assets/images/project-blest.jpg" alt="Obra Plaza Blest - Necsa Constructora" class="portfolio-img">
          <div class="portfolio-overlay">
            <span class="portfolio-tag">Comercial / Strip Center</span>
            <h3 class="portfolio-project-title">Plaza Blest</h3>
            <p class="portfolio-desc"><strong>Ubicación:</strong> San Miguel, Santiago | <strong>Superficie:</strong> 1.500 m²<br>Moderno centro comercial de locales estructurado en marcos de acero sismorresistente con paisajismo y exhibición de restos arqueológicos.</p>
          </div>
        </div>
        
        <!-- Proyecto 2: Casa Llantén (Residencial) -->
        <div class="portfolio-item" data-category="residenciales">
          <img src="assets/images/project-llanten.jpg" alt="Casa Llantén - Edificación Premium Necsa" class="portfolio-img">
          <div class="portfolio-overlay">
            <span class="portfolio-tag">Residencial Premium</span>
            <h3 class="portfolio-project-title">Casa Llantén</h3>
            <p class="portfolio-desc"><strong>Ubicación:</strong> Vitacura, Santiago | <strong>Superficie:</strong> 380 m²<br>Vanguardista residencia unifamiliar minimalista estructurada en hormigón visto y ventanales termopanel.</p>
          </div>
        </div>
        
        <!-- Proyecto 3: Car Market (Comercial/Industrial) -->
        <div class="portfolio-item" data-category="comerciales">
          <img src="assets/images/project-carmarket.jpg" alt="Car Market Showroom - Necsa Constructora" class="portfolio-img">
          <div class="portfolio-overlay">
            <span class="portfolio-tag">Comercial / Showroom</span>
            <h3 class="portfolio-project-title">Car Market</h3>
            <p class="portfolio-desc"><strong>Ubicación:</strong> Santiago | <strong>Superficie:</strong> 2.200 m²<br>Showroom de retail automotriz estructurado con pórticos metálicos pesados de grandes luces.</p>
          </div>
        </div>

        <!-- Proyecto 4: Obras Metro (Infraestructura) -->
        <div class="portfolio-item" data-category="comerciales">
          <img src="assets/images/project-metro.png" alt="Obras Metro - Necsa Constructora" class="portfolio-img">
          <div class="portfolio-overlay">
            <span class="portfolio-tag">Infraestructura / Transporte</span>
            <h3 class="portfolio-project-title">Obras Metro de Santiago</h3>
            <p class="portfolio-desc"><strong>Ubicación:</strong> Santiago | <strong>Especialidad:</strong> Refuerzo Estructural<br>Habilitación de espacios operacionales y refuerzos estructurales metálicos en estaciones subterráneas de alta afluencia.</p>
          </div>
        </div>

        <!-- Proyecto 5: Colegio San Gregorio (Educacional) -->
        <div class="portfolio-item" data-category="comerciales">
          <img src="assets/images/project-colegio.png" alt="Colegio San Gregorio - Necsa Constructora" class="portfolio-img">
          <div class="portfolio-overlay">
            <span class="portfolio-tag">Institucional / Educacional</span>
            <h3 class="portfolio-project-title">Colegio San Gregorio</h3>
            <p class="portfolio-desc"><strong>Ubicación:</strong> La Cisterna, Santiago | <strong>Especialidad:</strong> Ampliación y Obras Civiles<br>Ampliación de pabellón docente y mejoramiento de infraestructura civil para el Colegio San Gregorio de La Salle.</p>
          </div>
        </div>
        
      </div>
    </div>
  </section>"""

    replace_4 = """  <!-- --- SECCIÓN PORTAFOLIO (PROYECTOS) --- -->
  <section class="section" id="proyectos">
    <div class="container">
      <div class="section-title-wrapper" style="margin-bottom: var(--spacing-md);">
        <h2 class="section-title">Conoce algunos de nuestros proyectos</h2>
      </div>
      
      <!-- Filtros del Portafolio -->
      <div class="portfolio-filters">
        <button class="filter-btn active" data-filter="all">Todos los Proyectos</button>
        <button class="filter-btn" data-filter="residenciales">Residenciales Premium</button>
        <button class="filter-btn" data-filter="comerciales">Comerciales e Industriales</button>
      </div>
      
      <!-- Grid de Proyectos -->
      <div class="portfolio-grid">
        
        <!-- Proyecto 1: Plaza Blest (Comercial) -->
        <a href="#contacto" class="portfolio-item" data-category="comerciales">
          <img src="assets/images/project-blest.jpg" alt="Obra Plaza Blest - Necsa Constructora" class="portfolio-img">
          <div class="portfolio-overlay">
            <span class="portfolio-tag">Comercial / Strip Center</span>
            <h3 class="portfolio-project-title">Plaza Blest</h3>
            <p class="portfolio-desc"><strong>Ubicación:</strong> San Miguel, Santiago | <strong>Superficie:</strong> 1.500 m²<br>Moderno centro comercial de locales estructurado en marcos de acero sismorresistente con paisajismo y exhibición de restos arqueológicos.</p>
          </div>
        </a>
        
        <!-- Proyecto 2: Casa Llantén (Residencial) -->
        <a href="#contacto" class="portfolio-item" data-category="residenciales">
          <img src="assets/images/project-llanten.jpg" alt="Casa Llantén - Edificación Premium Necsa" class="portfolio-img">
          <div class="portfolio-overlay">
            <span class="portfolio-tag">Residencial Premium</span>
            <h3 class="portfolio-project-title">Casa Llantén</h3>
            <p class="portfolio-desc"><strong>Ubicación:</strong> Vitacura, Santiago | <strong>Superficie:</strong> 380 m²<br>Vanguardista residencia unifamiliar minimalista estructurada en hormigón visto y ventanales termopanel.</p>
          </div>
        </a>
        
        <!-- Proyecto 3: Car Market (Comercial/Industrial) -->
        <a href="#contacto" class="portfolio-item" data-category="comerciales">
          <img src="assets/images/project-carmarket.jpg" alt="Car Market Showroom - Necsa Constructora" class="portfolio-img">
          <div class="portfolio-overlay">
            <span class="portfolio-tag">Comercial / Showroom</span>
            <h3 class="portfolio-project-title">Car Market</h3>
            <p class="portfolio-desc"><strong>Ubicación:</strong> Santiago | <strong>Superficie:</strong> 2.200 m²<br>Showroom de retail automotriz estructurado con pórticos metálicos pesados de grandes luces.</p>
          </div>
        </a>

        <!-- Proyecto 4: Obras Metro (Infraestructura) -->
        <a href="#contacto" class="portfolio-item" data-category="comerciales">
          <img src="assets/images/project-metro.png" alt="Obras Metro - Necsa Constructora" class="portfolio-img">
          <div class="portfolio-overlay">
            <span class="portfolio-tag">Infraestructura / Transporte</span>
            <h3 class="portfolio-project-title">Obras Metro de Santiago</h3>
            <p class="portfolio-desc"><strong>Ubicación:</strong> Santiago | <strong>Especialidad:</strong> Refuerzo Estructural<br>Habilitación de espacios operacionales y refuerzos estructurales metálicos en estaciones subterráneas de alta afluencia.</p>
          </div>
        </a>

        <!-- Proyecto 5: Colegio San Gregorio (Educacional) -->
        <a href="#contacto" class="portfolio-item" data-category="comerciales">
          <img src="assets/images/project-colegio.png" alt="Colegio San Gregorio - Necsa Constructora" class="portfolio-img">
          <div class="portfolio-overlay">
            <span class="portfolio-tag">Institucional / Educacional</span>
            <h3 class="portfolio-project-title">Colegio San Gregorio</h3>
            <p class="portfolio-desc"><strong>Ubicación:</strong> La Cisterna, Santiago | <strong>Especialidad:</strong> Ampliación y Obras Civiles<br>Ampliación de pabellón docente y mejoramiento de infraestructura civil para el Colegio San Gregorio de La Salle.</p>
          </div>
        </a>
        
      </div>
    </div>
  </section>"""
    
    replacements.append((search_4, replace_4))

    # 5. Metrics Section
    search_5 = """  <!-- --- SECCIÓN MÉTRICAS --- -->
  <section class="metrics-section">
    <div class="metrics-bg"></div>
    <div class="container metrics-container">
      
      <div class="metric-item">
        <div class="metric-number">15+</div>
        <div class="metric-label">Años de Trayectoria</div>
      </div>
      
      <div class="metric-item">
        <div class="metric-number">250+</div>
        <div class="metric-label">Proyectos Entregados</div>
      </div>
      
      <div class="metric-item">
        <div class="metric-number">30k+</div>
        <div class="metric-label">m² Construidos en Acero</div>
      </div>
      
      <div class="metric-item">
        <div class="metric-number">100%</div>
        <div class="metric-label">Cumplimiento Legal OGUC</div>
      </div>
      
    </div>
  </section>"""

    replace_5 = """  <!-- --- SECCIÓN MÉTRICAS --- -->
  <section class="metrics-section">
    <div class="metrics-bg"></div>
    <div class="container metrics-container">
      
      <div class="metric-item">
        <div class="metric-number">12+</div>
        <div class="metric-label">Años de Trayectoria</div>
      </div>
      
      <div class="metric-item">
        <div class="metric-number">150+</div>
        <div class="metric-label">Proyectos Ejecutados</div>
      </div>
      
      <div class="metric-item">
        <div class="metric-number">300k+</div>
        <div class="metric-label">M² Proyectados de Mortero</div>
      </div>
      
    </div>
  </section>"""
    
    replacements.append((search_5, replace_5))

    # 6. Contacto Section
    search_6 = """  <!-- --- SECCIÓN CONTACTO --- -->
  <section class="section-alt" id="contacto">
    <div class="container">
      <div class="section-title-wrapper">
        <h2 class="section-title">Contáctenos</h2>
        <p class="section-subtitle">Ponte en contacto con nuestro equipo técnico para planificar y cotizar tu próximo proyecto de construcción o ingeniería.</p>
      </div>
      
      <div style="max-width: 600px; margin: 0 auto;">
        
        <!-- Formulario Interactivo -->
        <div class="contact-form-wrapper">
          <form id="necsa-contact-form" novalidate>
            
            <div class="form-group">
              <label for="form-nombre" class="form-label">Nombre Completo *</label>
              <input type="text" id="form-nombre" class="form-input" placeholder="Ej. Juan Pérez" required>
            </div>
            
            <div class="form-group-row">
              <div class="form-group">
                <label for="form-correo" class="form-label">Correo Electrónico *</label>
                <input type="email" id="form-correo" class="form-input" placeholder="juan@correo.cl" required>
              </div>
              <div class="form-group">
                <label for="form-telefono" class="form-label">Teléfono de Contacto *</label>
                <input type="tel" id="form-telefono" class="form-input" placeholder="Ej. +56 9 1234 5678" required>
              </div>
            </div>
            
 
            
            <button type="submit" class="btn btn-primary" style="width: 100%;">
              <i class="fa-solid fa-paper-plane"></i> Enviar Mensaje
            </button>
            
            <!-- Mensajes de Estado del Formulario -->
            <div id="form-alert" class="form-message"></div>
            
          </form>
        </div>
        
      </div>
    </div>
  </section>"""

    replace_6 = """  <!-- --- SECCIÓN CONTACTO --- -->
  <section class="section-alt" id="contacto">
    <div class="container">
      <div class="section-title-wrapper" style="margin-bottom: var(--spacing-lg);">
        <h2 class="section-title">Contacto</h2>
      </div>
      
      <div class="contact-grid">
        <!-- Información de Oficinas -->
        <div class="contact-info">
          <h3 style="font-family: var(--font-headings); font-size: 1.8rem; color: var(--color-primary); margin-bottom: 0.5rem;">Nuestras Oficinas</h3>
          <p class="contact-lead">Ponte en contacto con nuestro equipo técnico para planificar y cotizar tu próximo proyecto de construcción o ingeniería.</p>
          
          <div class="contact-details">
            <div class="contact-item">
              <div class="contact-icon"><i class="fa-solid fa-location-dot"></i></div>
              <div class="contact-text">
                <h4>Dirección</h4>
                <p>Av. Consistorial #5791 Of. 59, Peñalolén, Santiago</p>
              </div>
            </div>
            
            <div class="contact-item">
              <div class="contact-icon"><i class="fa-solid fa-envelope"></i></div>
              <div class="contact-text">
                <h4>Correo Electrónico</h4>
                <p>contacto@necsa.cl</p>
              </div>
            </div>
            
            <div class="contact-item">
              <div class="contact-icon"><i class="fa-regular fa-clock"></i></div>
              <div class="contact-text">
                <h4>Horario de Atención</h4>
                <p>Lun a Vie: 8:30 AM - 6:30 PM<br>Sáb: 9:00 AM - 1:00 PM</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Formulario Interactivo -->
        <div class="contact-form-wrapper">
          <h3 style="font-family: var(--font-headings); font-size: 1.5rem; color: var(--color-primary); margin-bottom: 1.5rem;">Cotiza con nosotros</h3>
          <form id="necsa-contact-form" novalidate>
            
            <div class="form-group">
              <label for="form-nombre" class="form-label">Nombre Completo *</label>
              <input type="text" id="form-nombre" class="form-input" placeholder="Ej. Juan Pérez" required>
            </div>
            
            <div class="form-group-row">
              <div class="form-group">
                <label for="form-correo" class="form-label">Correo Electrónico *</label>
                <input type="email" id="form-correo" class="form-input" placeholder="juan@correo.cl" required>
              </div>
              <div class="form-group">
                <label for="form-telefono" class="form-label">Teléfono de Contacto *</label>
                <input type="tel" id="form-telefono" class="form-input" placeholder="Ej. +56 9 1234 5678" required>
              </div>
            </div>
            
            <button type="submit" class="btn btn-primary" style="width: 100%;">
              <i class="fa-solid fa-paper-plane"></i> Enviar Mensaje
            </button>
            
            <!-- Mensajes de Estado del Formulario -->
            <div id="form-alert" class="form-message"></div>
            
          </form>
        </div>
      </div>
    </div>
  </section>"""
    
    replacements.append((search_6, replace_6))

    # 7. Footer Logo
    search_7 = """        <!-- Columna 1: Nosotros -->
        <div class="footer-about">
          <div class="logo">
            <img src="assets/images/logo-nuevo.png" alt="Logo Necsa" style="height: 55px; border-radius: var(--border-radius-sm); background-color: #fff; padding: 3px;">
            <div class="logo-text">
              <span class="logo-title footer-logo-title" style="color: #fff;">NECSA</span>
              <span class="logo-subtitle" style="color: rgba(255,255,255,0.65);">CONSTRUCTORA</span>
            </div>
          </div>"""

    replace_7 = """        <!-- Columna 1: Nosotros -->
        <div class="footer-about">
          <div class="logo">
            <img src="assets/images/logo%201%20con%20texto.png" alt="Logo Necsa" style="height: 55px; border-radius: var(--border-radius-sm); background-color: #fff; padding: 3px;">
          </div>"""
    
    replacements.append((search_7, replace_7))

    for idx, (search_str, replace_str) in enumerate(replacements, 1):
        if search_str in content:
            content = content.replace(search_str, replace_str)
            print(f"Applied replacement {idx} successfully!")
        else:
            # Let's try matching with normalized line endings
            normalized_search = search_str.replace('\r\n', '\n')
            normalized_content = content.replace('\r\n', '\n')
            if normalized_search in normalized_content:
                normalized_content = normalized_content.replace(normalized_search, replace_str.replace('\r\n', '\n'))
                content = normalized_content
                print(f"Applied replacement {idx} successfully (normalized endings)!")
            else:
                print(f"FAILED to find pattern {idx}!")

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    refactor_html()
