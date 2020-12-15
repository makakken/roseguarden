//parse entrries
export function parseEntries(view, viewDictionary) {
    if(viewDictionary.hasOwnProperty(view)) {
        return viewDictionary[view].entries;
    } else {
        return [];
    }
}

//parse entrries
export function parseProperties(view, viewDictionary) {
  let properties = {};
  let actionExist = false;
  if(viewDictionary.hasOwnProperty(view)) {
    viewDictionary[view].properties.forEach(function (item, index) {
      if(item.type !== 'action') {
        properties[item.name] = item;
      }
    });        
    return properties;
} else {
      return {};
  }
}

export function parseHeader(view, viewDictionary) {
    let headers = [];
    let actionExist = false;
    if(viewDictionary.hasOwnProperty(view)) {
      viewDictionary[view].properties.forEach(function (item, index) {
        if(item.type === 'action') {
          if(actionExist === false) {
            headers.push({ text: 'Actions',  value: 'actions', tooltip: item.label, action: item.action, name: item.name });
          }
          actionExist = true;
        } else {
          if(item.hide != true) {
            headers.push({ text: item.label,  value: item.name });
          }
        }
      });        
      return headers;
    } else {
      return [];
    }
  } 


export function parseActions(view, viewDictionary) {
  let actions = [];
  if(viewDictionary.hasOwnProperty(view)) {        
    console.log("-----", viewDictionary[view].entries);
    viewDictionary[view].properties.forEach(function (item, index) {
      if(item.type === 'action') {
        actions.push({ name: item.name, icon: item.icon, tooltip: item.label, action: item.action, color: item.color });
      }
    });        
    return actions;
  } else {
    return [];
  }
}