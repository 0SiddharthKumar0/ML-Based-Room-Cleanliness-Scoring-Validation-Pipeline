TABLE: users

id
name
email
password_hash
role
created_at

Roles:
- STAFF
- SUPERVISOR
- ADMIN


TABLE: rooms

id
room_number
floor
room_type
status
created_at


TABLE: room_inspections

id
room_id
staff_id

cleanliness_score
confidence_score

ml_decision
final_decision

supervisor_id

inspection_time
review_time


TABLE: inspection_images

id
inspection_id

image_path
image_type

uploaded_at

Image Types:
- BEFORE_CLEANING
- AFTER_CLEANING


TABLE: audit_logs

id

inspection_id

action
performed_by

old_value
new_value

created_at