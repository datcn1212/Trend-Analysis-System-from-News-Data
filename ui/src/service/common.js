import axios from "axios";

const API_ROOT = process.env.REACT_APP_API_ROOT || "http://localhost:5000";

const APIS = {
  // getOverviewInfo: () => axios.get(`${API_ROOT}/get_overview`),

  getAllKeywords: (args) =>
    axios.get(`${API_ROOT}/all_keywords`, { params: args }),

  getTopicKeywords: (topic, args) =>
    axios.get(`${API_ROOT}/topic_keywords/${topic}`, { params: args }),

  getCountTopic: (startTime, endTime) =>
    axios.get(`${API_ROOT}/count_topic`, {
      params: {
        startTime: startTime,
        endTime: endTime,
      },
    }),
};

export default APIS;
