from lib.models import create_role, create_audition, hire_actor, get_role_info

# Create a role
role = create_role("Hamlet")

# Create auditions
audition1 = create_audition("John Doe", "New York", 1234567890, role.id)
audition2 = create_audition("Jane Smith", "Los Angeles", 9876543210, role.id)

# Hire an actor
hire_actor(audition1.id)

# Fetch role details
get_role_info(role.id)
