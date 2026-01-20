const menu = [
    { title: "Inicio", path: "index.html" },
    {
        title: "Fundamentos",
        items: [
            { title: "Introducción", path: "01_introduccion.html" },
            { title: "Configuración", path: "02_configuracion.html" },
            { title: "Modelos Avanzados", path: "03_modelos.html" },
            { title: "Vistas y URLs (CBV)", path: "04_vistas_urls.html" },
            { title: "Plantillas", path: "05_plantillas.html" },
            { title: "Formularios", path: "06_formularios.html" },
            { title: "Autenticación", path: "09_autenticacion.html" },
            { title: "Admin Profesional", path: "07_admin.html" },
            { title: "Temas Avanzados", path: "08_avanzado.html" },
            { title: "Recursos", path: "recursos.html" },
        ]
    }
];

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
                    <span class="px-2 text-xs font-semibold text-gray-500 uppercase tracking-wider">
                        ${section.title}
                    </span>
                </li>
            `;
            section.items.forEach(item => {
                const isActive = currentPath === item.path;
                const activeClass = isActive
                    ? 'bg-blue-600 text-white shadow-md'
                    : 'text-gray-300 hover:bg-gray-800 hover:text-white';

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
                : 'text-gray-300 hover:bg-gray-800 hover:text-white';
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

document.addEventListener('DOMContentLoaded', () => {
    renderSidebar();

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
