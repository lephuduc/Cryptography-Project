package abac
import data.resource_attributes
import data.user_attributes

# User attributes

default allow = false

allow {
    user_input := input.user
    user := user_attributes[user_input]
    user.user_role == "admin"
}

allow {
    user := user_attributes[input.user]
    user.user_role == "manager"
    user.department == resource_attributes["Product"].resource_department
}

allow {
    user := user_attributes[input.user]
    user.user_role == "manager"
    user.department == resource_attributes["About"].resource_department
}