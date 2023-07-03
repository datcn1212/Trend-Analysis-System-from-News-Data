import axios from "axios";

const API_ROOT = process.env.REACT_APP_API_ROOT || "http://localhost:5000";

const APIS = {
  // getOverviewInfo: () => axios.get(`${API_ROOT}/get_overview`),

  getAllKeywords: (startTime, endTime) =>
    axios.get(`${API_ROOT}/all_keywords`, {
      params: {
        startTime: startTime,
        endTime: endTime,
      },
    }),

  getTopicKeywords: (topic, startTime, endTime) =>
    axios.get(`${API_ROOT}/topic_keywords/${topic}`, {
      params: {
        startTime: startTime,
        endTime: endTime,
      },
    }),

  getCountTopic: (startTime, endTime) =>
    axios.get(`${API_ROOT}/count_topic`, {
      params: {
        startTime: startTime,
        endTime: endTime,
      },
    }),

  getSearchData: (word) =>
    axios.get(`${API_ROOT}/search`, {
      params: {
        word: encodeURIComponent(word)
      },
    }),
};

export default APIS;
