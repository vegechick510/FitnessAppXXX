# Customized Dashboard

## Overview
The **Customized Dashboard** feature allows users to create a personalized view of their fitness journey by displaying and organizing essential widgets tailored to their needs. It enables users to track key metrics such as goal progress, workout reminders, fitness recipes, and more, all in one place. With this flexible and secure design, users can prioritize what matters most, ensuring a streamlined and effective fitness experience.

## Feature Details
- **Drag-and-Drop Widgets**: Users can rearrange widgets on their dashboard to reflect their preferences and focus on the aspects of health and fitness they value the most.
- **Key Metrics at a Glance**: The dashboard showcases essential widgets, including:
  - **Goal Progress Reminder**: Track progress visually with a dynamic progress bar.
  - **Workout Plan Reminder**: Stay on top of scheduled workouts.
  - **Fitness Recipes**: Discover healthy meal suggestions.
  - **Upcoming Meetings**: Keep track of scheduled fitness or health-related meetings.
  - And more customizable sections.
- **Secure Layout Saving**: The customized layout is securely stored, so users' preferences remain intact even after logging out.
- **Dynamic Updates**: Widgets update in real-time to reflect the latest data, providing an up-to-date snapshot of the user’s fitness journey.

## Benefits
- **Personalized Experience**: Tailor the dashboard to focus on specific goals and activities, making it uniquely suited to each user's fitness journey.
- **Convenient Tracking**: Consolidates key metrics in one location for quick and easy access.
- **Seamless Customization**: Drag-and-drop functionality ensures effortless rearrangement of widgets without technical expertise.
- **Consistency Across Sessions**: Securely saved preferences guarantee that the customized layout remains consistent, improving the user experience.
- **Motivation and Organization**: A centralized, well-organized dashboard empowers users to stay motivated and focused on their fitness goals.

## Implementation
- **Frontend Design**: The drag-and-drop functionality is implemented using `SortableJS` in `dashboard.html`.
- **Backend Support**: User preferences are stored securely in the database to ensure layout persistence across sessions.
- **Real-Time Updates**: Widgets are dynamically updated through AJAX calls, ensuring that the displayed data remains current.

## Usage
1. **Customize Your Dashboard**:
   - Log in to the app and navigate to the **Dashboard**.
   - Drag and drop widgets (e.g., **Goal Progress**, **Workout Plan Reminder**) to arrange them as per your preference.

2. **Save Preferences**:
   - The layout is saved automatically, ensuring your preferred arrangement persists across sessions.

3. **Track Your Progress**:
   - Monitor your progress at a glance with key widgets, such as the **Goal Progress Reminder** and **Workout Plan Reminder**.
   - Stay organized with additional widgets like **Fitness Recipes** and **Upcoming Meetings**.

4. **Enjoy a Personalized Experience**:
   - Log out and log back in to see your customized dashboard exactly how you left it, allowing you to pick up where you left off seamlessly.

