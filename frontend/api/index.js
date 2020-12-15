// implement your own methods in here, if your data is coming from A rest API

import * as User from './user';
import * as Chart from './chart';
import * as ActionBuilder from './actionBuilder'
import * as RequestBuilder from './requestBuilder'

export default {
  // user
  user : User,
  getUser: User.getUser,
  getUserById: User.getUserById,
  // chart data
  getMonthVisit: Chart.monthVisitData,
  getCampaign: Chart.campaignData,
  getLocation: Chart.locationData,
  actionBuilder: ActionBuilder,
  requestBuilder: RequestBuilder
};