package abac_test

import data.abac.allow

test_allow_is_false_by_default {
    not allow
}

test_allow_if_admin {
    allow with input as {
        "user": "duc"
    }
}

