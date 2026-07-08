/* 
  Necsa Constructora - Interactividad Principal
  Contiene:
  1. Efecto Scroll en Header y Navegación Activa Dinámica
  2. Menú de Navegación Móvil Hamburguesa
  3. Filtrado Interactivo del Portafolio con transiciones suaves
  4. Animación de Contadores de Métricas (Scroll-Triggered)
  5. Validación y Simulación de Formulario de Contacto Premium
*/

document.addEventListener('DOMContentLoaded', () => {
  
  /* ==========================================================================
     1. EFECTO SCROLL EN HEADER Y LINKS ACTIVOS
     ========================================================================== */
  const header = document.getElementById('header');
  const sections = document.querySelectorAll('section[id]');
  const navLinks = document.querySelectorAll('.nav-link');
  const heroActions = document.querySelector('.hero-actions');

  const handleScroll = () => {
    // 1.1 Cambiar fondo del header al hacer scroll
    if (window.scrollY > 50) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }

    // 1.1.b Expandir el logo (N -> NECSA) al acercarse al botón "Ver Obras Realizadas"
    if (heroActions) {
      const triggerPoint = heroActions.getBoundingClientRect().top + window.scrollY - 140;
      if (window.scrollY > triggerPoint) {
        header.classList.add('logo-expand');
      } else {
        header.classList.remove('logo-expand');
      }
    }

    // 1.2 Detectar sección activa en el menú
    let scrollY = window.pageYOffset;
    
    sections.forEach(current => {
      const sectionHeight = current.offsetHeight;
      const sectionTop = current.offsetTop - 120; // Offset para compensar el header
      const sectionId = current.getAttribute('id');
      
      if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
        navLinks.forEach(link => {
          link.classList.remove('active');
          if (link.getAttribute('href') === `#${sectionId}`) {
            link.classList.add('active');
          }
        });
      }
    });
  };
  
  window.addEventListener('scroll', handleScroll);
  handleScroll(); // Ejecutar al cargar para validar posición inicial

  /* ==========================================================================
     2. MENÚ DE NAVEGACIÓN MÓVIL (HAMBURGUESA)
     ========================================================================== */
  const navToggle = document.getElementById('nav-toggle');
  const navMenu = document.getElementById('nav-menu');
  
  if (navToggle && navMenu) {
    navToggle.addEventListener('click', () => {
      navToggle.classList.toggle('open');
      navMenu.classList.toggle('open');
    });
    
    // Cerrar menú móvil al hacer click en cualquier enlace de navegación
    navLinks.forEach(link => {
      link.addEventListener('click', () => {
        navToggle.classList.remove('open');
        navMenu.classList.remove('open');
      });
    });
  }

  /* ==========================================================================
     3. FILTRADO INTERACTIVO DEL PORTAFOLIO
     ========================================================================== */
  const filterButtons = document.querySelectorAll('.filter-btn');
  const portfolioItems = document.querySelectorAll('.portfolio-item');
  
  filterButtons.forEach(btn => {
    btn.addEventListener('click', (e) => {
      // 3.1 Activar botón clicado
      filterButtons.forEach(button => button.classList.remove('active'));
      btn.classList.add('active');
      
      const filterValue = btn.getAttribute('data-filter');
      
      // 3.2 Filtrar elementos con animación fluida
      portfolioItems.forEach(item => {
        item.style.transition = 'opacity 0.3s ease, transform 0.3s ease';
        
        // Fase 1: Desvanecer (Fade out)
        item.style.opacity = '0';
        item.style.transform = 'scale(0.95)';
        
        setTimeout(() => {
          const category = item.getAttribute('data-category');
          
          if (filterValue === 'all' || category === filterValue) {
            item.style.display = 'block';
            // Fase 2: Aparecer (Fade in con escala)
            setTimeout(() => {
              item.style.opacity = '1';
              item.style.transform = 'scale(1)';
            }, 50);
          } else {
            item.style.display = 'none';
          }
        }, 300); // Duración de la animación de fade out
      });
    });
  });

  /* ==========================================================================
     4. CARRUSEL DE FOTOS EN TARJETAS DE PROYECTOS
     ========================================================================== */
  portfolioItems.forEach(item => {
    const images = Array.from(item.querySelectorAll('.portfolio-img'));
    const dotsWrapper = item.querySelector('.carousel-dots');
    const prevBtn = item.querySelector('.carousel-prev');
    const nextBtn = item.querySelector('.carousel-next');

    if (images.length <= 1) {
      item.setAttribute('data-single', '');
      item.classList.add('is-first');
      return;
    }

    let current = images.findIndex(img => img.classList.contains('active'));
    if (current < 0) current = 0;
    item.classList.toggle('is-first', current === 0);

    // Generar puntos indicadores dinámicamente
    const dots = images.map((_, i) => {
      const dot = document.createElement('span');
      dot.className = 'dot' + (i === current ? ' active' : '');
      dot.addEventListener('click', (e) => {
        e.preventDefault();
        e.stopPropagation();
        goTo(i);
      });
      dotsWrapper.appendChild(dot);
      return dot;
    });

    function goTo(index) {
      images[current].classList.remove('active');
      dots[current].classList.remove('active');
      current = (index + images.length) % images.length;
      images[current].classList.add('active');
      dots[current].classList.add('active');
      item.classList.toggle('is-first', current === 0);
    }

    if (prevBtn) {
      prevBtn.addEventListener('click', (e) => {
        e.preventDefault();
        e.stopPropagation();
        goTo(current - 1);
      });
    }

    if (nextBtn) {
      nextBtn.addEventListener('click', (e) => {
        e.preventDefault();
        e.stopPropagation();
        goTo(current + 1);
      });
    }

    // Auto-avance suave cada 4.5s, pausado al pasar el mouse
    let autoplay = setInterval(() => goTo(current + 1), 4500);
    item.addEventListener('mouseenter', () => clearInterval(autoplay));
    item.addEventListener('mouseleave', () => {
      autoplay = setInterval(() => goTo(current + 1), 4500);
    });
  });

  /* ==========================================================================
     4.b ANIMACIÓN DE CONTADORES DE MÉTRICAS (SCROLL-TRIGGERED)
     ========================================================================== */
  const statNumbers = document.querySelectorAll('.stat-number');

  if (statNumbers.length) {
    const animateCount = (el) => {
      const target = parseInt(el.getAttribute('data-target'), 10) || 0;
      const suffix = el.getAttribute('data-suffix') || '';
      const duration = 1800;
      const startTime = performance.now();

      const step = (now) => {
        const progress = Math.min((now - startTime) / duration, 1);
        const eased = 1 - Math.pow(1 - progress, 3); // ease-out cúbico
        const current = Math.round(target * eased);
        el.textContent = current + suffix;

        if (progress < 1) {
          requestAnimationFrame(step);
        }
      };

      requestAnimationFrame(step);
    };

    const statsObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          animateCount(entry.target);
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.4 });

    statNumbers.forEach(el => statsObserver.observe(el));
  }

  /* ==========================================================================
     5. FORMULARIO DE CONTACTO PREMIUM (VALIDACIÓN Y SIMULACIÓN)
     ========================================================================== */
  const contactForm = document.getElementById('necsa-contact-form');
  const formAlert = document.getElementById('form-alert');
  
  if (contactForm && formAlert) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();
      
      // 5.1 Resetear alertas
      formAlert.className = 'form-message';
      formAlert.style.display = 'none';
      
      // 5.2 Obtener campos y valores
      const nombre = document.getElementById('form-nombre');
      const correo = document.getElementById('form-correo');
      const telefono = document.getElementById('form-telefono');
      
      // 5.3 Validaciones
      let errors = [];
      
      if (!nombre.value.trim()) {
        errors.push("El nombre es requerido.");
        nombre.style.borderColor = 'var(--color-error)';
      } else {
        nombre.style.borderColor = 'var(--color-secondary-light)';
      }
      
      const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!correo.value.trim() || !emailPattern.test(correo.value.trim())) {
        errors.push("Ingresa un correo electrónico válido.");
        correo.style.borderColor = 'var(--color-error)';
      } else {
        correo.style.borderColor = 'var(--color-secondary-light)';
      }
      
      if (!telefono.value.trim()) {
        errors.push("El teléfono es requerido.");
        telefono.style.borderColor = 'var(--color-error)';
      } else {
        telefono.style.borderColor = 'var(--color-secondary-light)';
      }
      
      // Mostrar errores si existen
      if (errors.length > 0) {
        formAlert.innerHTML = `<i class="fa-solid fa-triangle-exclamation"></i> <strong>Error de validación:</strong><br>${errors.join('<br>')}`;
        formAlert.classList.add('error');
        return;
      }
      
      // 5.4 Simular envío de datos a servidor (con loader premium en el botón)
      const submitBtn = contactForm.querySelector('button[type="submit"]');
      const originalBtnHtml = submitBtn.innerHTML;
      
      submitBtn.disabled = true;
      submitBtn.innerHTML = `<i class="fa-solid fa-circle-notch fa-spin"></i> Procesando solicitud...`;
      
      setTimeout(() => {
        // Éxito simulado
        submitBtn.innerHTML = `<i class="fa-solid fa-circle-check"></i> ¡Enviado con Éxito!`;
        submitBtn.style.backgroundColor = 'var(--color-success)';
        
        formAlert.innerHTML = `<i class="fa-solid fa-circle-check"></i> ¡Gracias, <strong>${nombre.value}</strong>! Hemos recibido tu solicitud. Uno de nuestros ingenieros se contactará contigo al teléfono <strong>${telefono.value}</strong> o correo <strong>${correo.value}</strong> en un plazo menor a 24 horas laborables.`;
        formAlert.classList.add('success');
        
        // Limpiar formulario
        contactForm.reset();
        
        // Restaurar botón después de 3 segundos
        setTimeout(() => {
          submitBtn.disabled = false;
          submitBtn.innerHTML = originalBtnHtml;
          submitBtn.style.backgroundColor = '';
        }, 4000);
        
      }, 1500); // 1.5 segundos de carga simulada
    });
  }
});
