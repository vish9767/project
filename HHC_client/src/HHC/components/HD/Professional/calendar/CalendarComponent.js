import React, { useState, useEffect } from "react";
import { Calendar, momentLocalizer } from "react-big-calendar";
import moment from "moment";
import EventModal from "./EventModal";
import EventDetailsModal from "./EventDetailsModal";
import 'react-big-calendar/lib/css/react-big-calendar.css';
import "./Calender.css";
import Tooltip from "@mui/material/Tooltip";

const localizer = momentLocalizer(moment);

function convertTo12HourFormat(hours, minutes) {
  const period = hours >= 12 ? 'PM' : 'AM';
  const twelveHourFormatHours = hours % 12 || 12;
  return `${twelveHourFormatHours}:${minutes.toString().padStart(2, '0')} ${period}`;
}

const CalendarComponent = ({ events }) => {
  const [newEvents, setNewEvents] = useState([]);
  const [selectedEvent, setSelectedEvent] = useState(null);
  const [isEventModalOpen, setIsEventModalOpen] = useState(false);
  const [isEventDetailsModalOpen, setIsEventDetailsModalOpen] = useState(false);
  const [isEditingEvent, setIsEditingEvent] = useState(false);
  const [startTime, setStartTime] = useState('');
  const [endTime, setEndTime] = useState('');
  const [profID, setProfID] = useState(null);

  console.log("Individual Professional Event: ", events)
  useEffect(() => {
    if (events.length > 0) {
      const firstItem = events[0];
      const selectedProf = firstItem.srv_prof_id;
      setProfID(selectedProf);

      const startTime = firstItem.actual_StartDate_Time;
      const startDateObject = new Date(startTime);
      const startHours = startDateObject.getUTCHours();
      const startMinutes = startDateObject.getUTCMinutes();
      const start12HourFormat = convertTo12HourFormat(startHours, startMinutes);
      setStartTime(start12HourFormat);

      const endTime = firstItem.actual_EndDate_Time;
      const endDateObject = new Date(endTime);
      const endHours = endDateObject.getUTCHours();
      const endMinutes = endDateObject.getUTCMinutes();
      const end12HourFormat = convertTo12HourFormat(endHours, endMinutes);
      setEndTime(end12HourFormat);
      console.log("Start Time", start12HourFormat);
      console.log("End Time", end12HourFormat);
    }
  }, [events]);


  // useEffect(() => {
  //   fetchEvents();
  // }, []);

  // const fetchEvents = async () => {
  //   try {
  //     const response = await fetch("/api/events");
  //     setNewEvents(response.data);
  //   } catch (error) {
  //     console.error("Error fetching events:", error);
  //   }
  // };

  const handleEventSelect = (event) => {
    setSelectedEvent(event);
    setIsEventDetailsModalOpen(true);
  };

  // const handleEventModalOpen = () => {
  //   setSelectedEvent(null);
  //   setIsEventModalOpen(true);
  // };

  const handleEventModalOpen = (slotInfo) => {
    setSelectedEvent(null);
    setProfID(slotInfo.profID); // Assuming you can get the profID from slotInfo
    setIsEventModalOpen(true);
  };

  // const handleEventModalClose = () => {
  //   setIsEventModalOpen(false);
  // };

  const handleEventModalClose = () => {
    setIsEventModalOpen(false);
    setIsEditingEvent(false);
    // fetchEvents(); // Refresh the events after any CRUD operation
  };

  const handleEventDetailsModalClose = () => {
    setIsEventDetailsModalOpen(false);
  };

  const handleEventEdit = (event) => {
    setSelectedEvent(event);
    setIsEditingEvent(true);
    setIsEventModalOpen(true);
  };

  // Specify the views you want to display (excluding "agenda")
  const views = {
    month: true,
    week: true,
    day: true,
  };

  return (
    <div>
      <Calendar
        localizer={localizer}
        events={events.map((event) => ({
          ...event,
          title: `${startTime} - ${endTime}`,
        }))}
        startAccessor="start_date"
        endAccessor="end_date"
        selectable
        onSelectEvent={handleEventEdit} // Open modal for editing
        onSelectSlot={handleEventModalOpen} // Open modal for creating
        views={views}
      />

      <EventModal
        isOpen={isEventModalOpen}
        onClose={handleEventModalClose}
        // fetchEvents={fetchEvents}
        profEvent={profID}
      />
      {/* <EventDetailsModal
        event={selectedEvent}
        isOpen={isEventDetailsModalOpen}
        onClose={handleEventDetailsModalClose}
        fetchEvents={fetchEvents}
      /> */}
    </div>
  )
}

export default CalendarComponent
