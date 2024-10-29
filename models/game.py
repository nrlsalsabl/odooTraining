from odoo import models, fields, api # type: ignore

class Game(models.Model):
    _name = 'my_module.game'
    _description = 'Exercise menu game'

    name = fields.Char(string="Hero Name", required=True)
    role_id = fields.Many2one('my_module.role', string="Role", required=True)
    weapon_ids = fields.Many2many('my_module.weapon', string="Weapon")
    weightTotal = fields.Float(compute='_compute_weight_total', store=True)

    @api.depends('weapon_ids.weight')
    def _compute_weight_total(self):
        for record in self:
            total_weight = sum(weapon.weight for weapon in record.weapon_ids)
            record.weightTotal = total_weight

class Role(models.Model):
    _name = 'my_module.role'
    _description = 'Role of Hero'

    nameRole = fields.Char(string="Enter Role Name", required=True)

    def name_get(self):
        result = []
        for record in self:
            result.append((record.id, record.nameRole))
        return result

class Weapon(models.Model):
    _name = 'my_module.weapon'
    _description = 'Weapon of Hero'

    nameWeapon = fields.Char(string="Enter Weapon Name", required=True)
    weight = fields.Float(string="Weight")

    def name_get(self):
        result = []
        for record in self:
            result.append((record.id, record.nameWeapon))
        return result