from django import template

register = template.Library()

@register.filter
def status_color(status):
    # Assign specific classes based on job status
    colors = {
        "open": "text-green-600 border-green-600 bg-green-100",      # Green for "Open"
        "in_progress": "text-yellow-600 border-yellow-600 bg-yellow-100",  # Yellow for "In Progress"
        "completed": "text-blue-600 border-blue-600 bg-blue-100",    # Blue for "Completed"
    }
    return colors.get(status, "text-gray-600 border-gray-600 bg-gray-100")  # Default to gray
