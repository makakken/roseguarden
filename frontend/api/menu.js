const MenuStaticAppend = [
  { divider: true },
  { header: 'Konglomerat e.V.' },
  {
    title: 'Konglomerat',
    group: 'links',
    icon: 'home',
    external: true,
    href: 'https://konglomerat.org/'
  }
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
