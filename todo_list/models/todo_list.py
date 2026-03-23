from odoo import models, fields, api
from odoo.exceptions import ValidationError


class TodoList(models.Model):
    _name = 'todo.list'
    _description = 'Todo List'

    name = fields.Char(string='Title', required=True)
    tag_ids = fields.Many2many('todo.tag', string='Tags')
    start_date = fields.Date(string='Start Date', required=True)
    end_date = fields.Date(string='End Date', required=True)
    status = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('complete', 'Complete'),
    ], string='Status', default='draft')
    item_ids = fields.One2many('todo.item', 'todo_list_id', string='Todo Items')
    attendee_ids = fields.One2many('todo.attendee', 'todo_list_id', string='Attendees')
    all_items_done = fields.Boolean(compute='_compute_all_items_done', store=False)

    @api.constrains('start_date', 'end_date')
    def _check_dates(self):
        for rec in self:
            if rec.start_date and rec.end_date and rec.end_date <= rec.start_date:
                raise ValidationError('End Date must be later than Start Date.')

    @api.depends('item_ids.is_finished', 'item_ids')
    def _compute_all_items_done(self):
        for rec in self:
            if rec.item_ids:
                rec.all_items_done = all(item.is_finished for item in rec.item_ids)
            else:
                rec.all_items_done = False

    def action_start(self):
        self.status = 'in_progress'

    def action_complete(self):
        self.status = 'complete'


class TodoItem(models.Model):
    _name = 'todo.item'
    _description = 'Todo Item'

    name = fields.Char(string='Item Name', required=True)
    description = fields.Text(string='Description')
    is_finished = fields.Boolean(string='Finished')
    todo_list_id = fields.Many2one('todo.list', string='Todo List', ondelete='cascade')


class TodoTag(models.Model):
    _name = 'todo.tag'
    _description = 'Todo Tag'

    name = fields.Char(string='Tag Name', required=True)


class TodoAttendee(models.Model):
    _name = 'todo.attendee'
    _description = 'Todo Attendee'

    user_id = fields.Many2one('res.users', string='User Name', required=True)
    todo_list_id = fields.Many2one('todo.list', string='Todo List', ondelete='cascade')