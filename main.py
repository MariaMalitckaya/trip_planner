import * as st
import time  # For simulating agent processing

# 1. Define data structures (basic example)
class Location:
    def __init__(self, name, description, image_url=None, latitude=None, longitude=None):
        self.name = name
        self.description = description
        self.image_url = image_url
        self.latitude = latitude
        self.longitude = longitude

class Activity:
    def __init__(self, name, description, location=None, time_needed=None):
        self.name = name
        self.description = description
        self.location = location
        self.time_needed = time_needed

class DailyPlan:
    def __init__(self, day, activities):
        self.day = day
        self.activities = activities

class TripPlan:
    def __init__(self, destination, duration, daily_plans):
        self.destination = destination
        self.duration = duration
        self.daily_plans = daily_plans

# 2. AI Agent (Simplified - Rule-Based)
def generate_trip_plan(destination, duration, interests, pace, budget=None):
    """
    Generates a trip plan based on user preferences.
    This is a simplified, rule-based example.
    """
    time.sleep(2) # Simulate agent thinking
    if destination.lower() == "paris":
        locations = [
            Location("Eiffel Tower", "Iconic symbol of Paris.", "https://via.placeholder.com/150", 48.8584, 2.2945),
            Location("Louvre Museum", "Home to the Mona Lisa.", "https://via.placeholder.com/150", 48.8606, 2.3376),
            Location("Notre-Dame Cathedral", "A masterpiece of Gothic architecture.", "https://via.placeholder.com/150", 48.8525, 2.3490),
        ]
        if duration == 1:
            daily_plans = [
                DailyPlan(1, [
                    Activity("Visit Eiffel Tower", "Take in the views.", locations[0], 2),
                    Activity("See Mona Lisa", "At the Louvre.", locations[1], 3),
                ])
            ]
        elif duration == 2:
             daily_plans = [
                DailyPlan(1, [
                    Activity("Visit Eiffel Tower", "Take in the views.", locations[0], 2),
                    Activity("See Mona Lisa", "At the Louvre.", locations[1], 3),
                ]),
                DailyPlan(2, [
                    Activity("Explore Notre Dame", "Admire the architecture", locations[2], 2)
                ])
            ]
        else:
            daily_plans = [
                DailyPlan(1, [
                    Activity("Visit Eiffel Tower", "Take in the views.", locations[0], 2),
                    Activity("See Mona Lisa", "At the Louvre.", locations[1], 3),
                ]),
                DailyPlan(2, [
                    Activity("Explore Notre Dame", "Admire the architecture", locations[2], 2)
                ]),
                DailyPlan(3, [
                    Activity("Visit some cafe", "Enjoy the local food", locations[2], 2)
                ])
            ]
        return TripPlan(destination, duration, daily_plans)
    elif destination.lower() == "rome":
        locations = [
                Location("Colosseum", "Ancient Roman amphitheater.", "https://via.placeholder.com/150", 41.8902, 12.4922),
                Location("Roman Forum", "Center of ancient Rome.", "https://via.placeholder.com/150", 41.8925, 12.4852),
                Location("Pantheon", "A former Roman temple.", "https://via.placeholder.com/150", 41.8996, 12.4769),
            ]
        if duration == 1:
            daily_plans = [
                DailyPlan(1, [
                    Activity("Visit Colosseum", "Explore the amphitheater.", locations[0], 2),
                    Activity("See Roman Forum", "Explore the ancient ruins.", locations[1], 3),
                ])
            ]
        elif duration == 2:
             daily_plans = [
                DailyPlan(1, [
                    Activity("Visit Colosseum", "Explore the amphitheater.", locations[0], 2),
                    Activity("See Roman Forum", "Explore the ancient ruins.", locations[1], 3),
                ]),
                DailyPlan(2, [
                    Activity("Visit Pantheon", "Admire the architecture", locations[2], 2)
                ])
            ]
        else:
            daily_plans = [
                DailyPlan(1, [
                    Activity("Visit Colosseum", "Explore the amphitheater.", locations[0], 2),
                    Activity("See Roman Forum", "Explore the ancient ruins.", locations[1], 3),
                ]),
                DailyPlan(2, [
                    Activity("Visit Pantheon", "Admire the architecture", locations[2], 2)
                ]),
                DailyPlan(3, [
                    Activity("Visit some cafe", "Enjoy the local food", locations[2], 2)
                ])
            ]
        return TripPlan(destination, duration, daily_plans)
    else:
        return None # Indicate no plan can be generated

# 3. Streamlit App
def main():
    st.title("AI Trip Planner")

    # User Input
    destination = st.text_input("Enter your destination:", "Paris")
    duration = st.slider("Select the duration of your trip (days):", 1, 7, 3)
    interests = st.multiselect("Select your interests:", ["Historical Sites", "Beaches", "Food", "Art", "Nature", "Shopping"], default=["Historical Sites", "Food"])
    pace = st.radio("Select your preferred pace:", ["Relaxed", "Moderate", "Fast-Paced"], index=1) # Changed default to 1, which is "Moderate"
    budget = st.number_input("Enter your budget (optional):", min_value=0, format="%d")

    if st.button("Generate Trip Plan"):
        with st.spinner("Generating your trip plan..."):
            trip_plan = generate_trip_plan(destination, duration, interests, pace, budget)

        if trip_plan:
            st.header(f"Your Trip to {trip_plan.destination} ({trip_plan.duration} days)")
            for daily_plan in trip_plan.daily_plans:
                st.subheader(f"Day {daily_plan.day}")
                for activity in daily_plan.activities:
                    st.markdown(f"**{activity.name}**")
                    if activity.location and activity.location.image_url:
                        st.image(activity.location.image_url, caption=activity.location.name, width=300)
                    if activity.location:
                        st.write(f"Location: {activity.location.name}")
                    st.write(activity.description)
                    st.write(f"Time needed: {activity.time_needed} hours")
                    st.write("---")
        else:
            st.error(f"Could not generate a trip plan for {destination}. Please try a different destination.")

if __name__ == "__main__":
    main()