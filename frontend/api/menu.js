const MenuStaticAppend = [
  {divider: true},
  {header: 'Tools & Links'},
  { 
    title: 'Emulator',
    group: 'links', 
    icon: 'touch_app',
    external: true,
    href: 'https://rosemockup.fabba.space/door'
  },
];

// reorder menu
MenuStaticAppend.forEach((item) => {
  if (item.items) {
    item.items.sort((x, y) => {
      let textA = x.title.toUpperCase();
      let textB = y.title.toUpperCase();
      return (textA < textB) ? -1 : (textA > textB) ? 1 : 0;
    });
  }
});

export default {
  MenuStaticAppend
}
