const menu = [
    { title: "Inicio", path: "index.html" },
    {
        title: "Fundamentos",
        items: [
            { title: "1. Introducción", path: "01_introduccion.html" },
            { title: "2. Configuración", path: "02_configuracion.html" },
            { title: "3. Modelos Avanzados", path: "03_modelos.html" },
            { title: "4. Vistas y URLs", path: "04_vistas_urls.html" },
            { title: "5. Plantillas", path: "05_plantillas.html" },
            { title: "6. Formularios", path: "06_formularios.html" },
            { title: "7. Admin Profesional", path: "07_admin.html" },
            { title: "8. Temas Avanzados", path: "08_avanzado.html" },
            { title: "9. Autenticación", path: "09_autenticacion.html" },
        ]
    },
    {
        title: "Nivel Profesional",
        items: [
            { title: "10. Arquitectura Moderna", path: "10_arquitectura.html" },
            { title: "11. Patrones de Diseño", path: "11_patrones.html" },
            { title: "12. Arquitectura Avanzada", path: "12_arquitectura_avanzada.html" },
            { title: "13. DevOps y Calidad", path: "13_devops.html" },
            { title: "Recursos", path: "recursos.html" },
        ]
    },
    {
        title: "Proyectos Reales",
        items: [
            { title: "14. Setup del Proyecto", path: "14_proyecto_setup.html" },
            { title: "15. Autenticación y Login", path: "15_proyecto_auth.html" },
            { title: "16. Roles y Permisos", path: "16_proyecto_roles.html" },
            { title: "17. Dashboard ERP", path: "17_proyecto_erp.html" },
        ]
    }
];

// --- Sidebar & Menu Rendering ---

function renderSidebar() {
    const sidebar = document.getElementById('sidebar-content');
    if (!sidebar) return;

    // Get current filename, default to index.html if empty (root)
    const currentPath = window.location.pathname.split('/').pop() || 'index.html';

    let html = '<ul class="space-y-2 font-medium">';

    menu.forEach(section => {
        if (section.items) {
            html += `
                <li class="mt-6 mb-2">
                    <span class="px-2 text-xs font-semibold text-gray-500 uppercase tracking-wider dark:text-gray-400">
                        ${section.title}
                    </span>
                </li>
            `;
            section.items.forEach(item => {
                const isActive = currentPath === item.path;
                const activeClass = isActive
                    ? 'bg-blue-600 text-white shadow-md'
                    : 'text-gray-600 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-800 hover:text-blue-600 dark:hover:text-blue-400';

                html += `
                    <li>
                        <a href="${item.path}" class="flex items-center p-2 rounded-lg transition-colors duration-200 ${activeClass}">
                            <span class="ml-3">${item.title}</span>
                        </a>
                    </li>
                `;
            });
        } else {
             const isActive = currentPath === section.path;
             const activeClass = isActive
                ? 'bg-blue-600 text-white shadow-md'
                : 'text-gray-600 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-800 hover:text-blue-600 dark:hover:text-blue-400';
            html += `
                <li>
                    <a href="${section.path}" class="flex items-center p-2 rounded-lg transition-colors duration-200 ${activeClass}">
                        <span class="ml-3">${section.title}</span>
                    </a>
                </li>
            `;
        }
    });

    html += '</ul>';
    sidebar.innerHTML = html;
}

// --- Navigation Buttons (Prev/Next) ---

function renderNavigation() {
    const currentPath = window.location.pathname.split('/').pop() || 'index.html';

    // Flatten menu to find prev/next
    const flatMenu = [];
    menu.forEach(item => {
        if (item.items) {
            item.items.forEach(subItem => flatMenu.push(subItem));
        } else {
            flatMenu.push(item);
        }
    });

    const currentIndex = flatMenu.findIndex(item => item.path === currentPath);
    if (currentIndex === -1) return;

    const prevItem = currentIndex > 0 ? flatMenu[currentIndex - 1] : null;
    const nextItem = currentIndex < flatMenu.length - 1 ? flatMenu[currentIndex + 1] : null;

    const mainElement = document.querySelector('main');
    if (!mainElement) return;

    const navContainer = document.createElement('div');
    navContainer.className = 'mt-12 flex justify-between items-center pt-6 border-t border-gray-200 dark:border-gray-700';

    let prevHtml = prevItem
        ? `<a href="${prevItem.path}" class="flex items-center text-gray-600 hover:text-blue-600 dark:text-gray-400 dark:hover:text-blue-400 transition-colors">
             <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path></svg>
             <div>
                <span class="text-xs text-gray-400 uppercase">Anterior</span><br>
                <span class="font-medium">${prevItem.title}</span>
             </div>
           </a>`
        : `<div></div>`;

    let nextHtml = nextItem
        ? `<a href="${nextItem.path}" class="flex items-center text-right text-gray-600 hover:text-blue-600 dark:text-gray-400 dark:hover:text-blue-400 transition-colors">
             <div>
                <span class="text-xs text-gray-400 uppercase">Siguiente</span><br>
                <span class="font-medium">${nextItem.title}</span>
             </div>
             <svg class="w-5 h-5 ml-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
           </a>`
        : `<div></div>`;

    navContainer.innerHTML = prevHtml + nextHtml;
    mainElement.appendChild(navContainer);
}

// --- Dark Mode Logic ---

function initDarkMode() {
    const html = document.documentElement;
    const isDark = localStorage.getItem('theme') === 'dark' ||
                   (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches);

    if (isDark) {
        html.classList.add('dark');
    } else {
        html.classList.remove('dark');
    }

    // Inject Fixed Toggle Button (Top Right)
    const toggleBtn = document.createElement('button');
    toggleBtn.className = "fixed top-4 right-4 z-50 w-9 h-9 flex items-center justify-center rounded-full bg-gray-200 dark:bg-gray-700 text-gray-800 dark:text-gray-200 shadow-lg hover:bg-gray-300 dark:hover:bg-gray-600 transition-all focus:outline-none";
    toggleBtn.setAttribute('aria-label', 'Alternar modo oscuro');

    toggleBtn.innerHTML = isDark
        ? '<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>'
        : '<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 24.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"></path></svg>';

    toggleBtn.onclick = () => {
        const isDarkModeNow = html.classList.contains('dark');
        if (isDarkModeNow) {
            html.classList.remove('dark');
            localStorage.setItem('theme', 'light');
            toggleBtn.innerHTML = '<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 24.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"></path></svg>';
        } else {
            html.classList.add('dark');
            localStorage.setItem('theme', 'dark');
            toggleBtn.innerHTML = '<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>';
        }
    };

    document.body.appendChild(toggleBtn);
}


document.addEventListener('DOMContentLoaded', () => {
    initDarkMode();
    renderSidebar();
    renderNavigation();

    // Mobile menu toggle logic
    const toggleBtn = document.getElementById('mobile-menu-toggle');
    const sidebar = document.getElementById('default-sidebar');
    const overlay = document.getElementById('sidebar-overlay');

    if (toggleBtn && sidebar && overlay) {
        function toggleMenu() {
            const isClosed = sidebar.classList.contains('-translate-x-full');
            if (isClosed) {
                sidebar.classList.remove('-translate-x-full');
                overlay.classList.remove('hidden');
            } else {
                sidebar.classList.add('-translate-x-full');
                overlay.classList.add('hidden');
            }
        }

        toggleBtn.addEventListener('click', toggleMenu);
        overlay.addEventListener('click', toggleMenu);
    }
});
