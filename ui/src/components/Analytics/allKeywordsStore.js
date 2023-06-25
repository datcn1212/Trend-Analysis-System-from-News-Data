import { action, makeObservable, observable } from "mobx";
import _ from "lodash";
import APIS from "../../service/common";

class AllKeywordsStore {
  async fetchAllKeywords(startTime, endTime) { 
    const res = await APIS.getAllKeywords(startTime, endTime)
    return Object.entries(res.data).map(([x, y]) => ({ x, y }));
  }
}

export default new AllKeywordsStore();
