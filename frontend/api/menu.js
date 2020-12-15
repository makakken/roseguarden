const Menu = [
  {header: 'roseguarden'},
  {
    title: 'Home',
    group: 'apps',
    icon: 'dashboard',
    name: 'Dashboard',
    href: 'dashboard'
  },
  {divider: true},
  {header: 'Templates&Links'},
  { 
    title: 'Vue Material Admin',
    group: 'links', 
    icon: 'touch_app',
    external: true,
    href: 'https://github.com/tookit/vue-material-admin'
  },
  { 
    title: 'Vue Material Admin Demo',
    group: 'links', 
    icon: 'touch_app',
    external: true,
    href: 'http://vma.isocked.com/#/dashboard'
  },    
  {
    title: 'Vuetify',
    group: 'links',
    icon: 'touch_app',
    external: true,
    href: 'https://vuetifyjs.com/en/getting-started/quick-start'
  },    
];
// reorder menu
Menu.forEach((item) => {
  if (item.items) {
    item.items.sort((x, y) => {
      let textA = x.title.toUpperCase();
      let textB = y.title.toUpperCase();
      return (textA < textB) ? -1 : (textA > textB) ? 1 : 0;
    });
  }
});

export default Menu;
