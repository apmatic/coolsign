from odoo import api, fields, models

class HrEmployee(models.Model):
	_inherit = "hr.employee"

	enable_coolsign_app = fields.Boolean("Enable Coolsign App", groups="hr.group_hr_user")
	coolsign_app_id = fields.Char(string="Coolsign App ID", groups="hr.group_hr_user")

	def _employee_info(self, employee):
		"Build dictionary of the employee data."
		return {'id': employee.id,
				'enable_coolsign_app': employee.enable_coolsign_app,
				'coolsign_app_id': employee.coolsign_app_id,
				'name': employee.name,
				'attendance_state': employee.attendance_state,
				'last_check_in': employee.last_check_in,
				'last_check_out': employee.last_check_out}

	@api.model
	def get_employee_info(self):
		"Return dictionary of employee data."
		employee = self.env.user.employee_id
		return self._employee_info(employee)

	@api.model
	def add_attendance(self, position, coolsign_app_id):
		"""
		Insert attendance with position, checking the coolsign app id of the
		employee. Return dictionary with error key, in any, and employee data
		if insert is successful.
		"""
		employee = self.env.user.employee_id
		if not employee.enable_coolsign_app:
			return {'error': 'coolsign_app_disabled'}
		if employee.coolsign_app_id != coolsign_app_id:
			return {'error': 'coolsign_id_error'}
		pos = {'longitude': position['longitude'], 'latitude': position['latitude']}
		attendance = employee._attendance_action_change(pos)
		return {'error': '', 'employee': self._employee_info(employee)}

	@api.model
	def save_uuid(self, uuid):
		"Update the coolsign app id of the employee."
		employee = self.env.user.employee_id
		employee.coolsign_app_id = uuid
		return True
