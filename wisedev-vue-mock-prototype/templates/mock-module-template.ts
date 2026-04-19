export const featureHandlers = {
  list: () => ({
    code: 'SUCCESS',
    message: 'ok',
    data: {
      items: [],
      page: { pageNo: 1, pageSize: 20, total: 0 },
    },
  }),
}
