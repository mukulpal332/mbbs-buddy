export const generateRevisionSchedule = (startDate) => {
  const intervals = [1, 3, 7, 15, 30, 60, 90];
  return intervals.map(days => {
    const date = new Date(startDate);
    date.setDate(date.getDate() + days);
    return { day: `Day ${days}`, date: date.toISOString().split("T")[0] };
  });
};