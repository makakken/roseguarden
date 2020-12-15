function newBaseRequest() {
  let request = Object();
  request.head = {};
  request.head.version = "1.0";
  request.head.msgId = 1;
  request.head.requestType = "";
  request.head.target = "server";
  request.head.source = "client";
  request.actions = [];
  return request;
}

// action to login with username and password
function newActionRequest(actions, data) {
  let request = newBaseRequest();
  request.actions = actions;
  return request;
}


export default {
  newActionRequest,
};
