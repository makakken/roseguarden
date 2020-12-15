//parse entrries
export function cancelTableDialogs(refs, tablerefname) {
    if(refs.hasOwnProperty(tablerefname)){
        var dialogs = refs[tablerefname].$children[0].$children[0].$children;
        for(var i = 0; i < dialogs.length; i++) {
          if(dialogs[i].hasOwnProperty('cancel')) {
            dialogs[i].cancel();
          }
        }
      }
}