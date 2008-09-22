# gigkeeper
# Copyright (C) 2008 gigkeeper
#
# $Id$
#

from modu.util import theme, tags

class GigkeeperTheme(theme.Theme):
	def theme_note_list(self, form_id, element):
		content = ''
		for child_id in element:
			child = element[child_id]
			thm = child.get_theme(self.req, current=self)
		
			theme_func = getattr(thm, 'theme_' + child.attr('type', 'fieldset'))
			
			content += tags.div()[theme_func(element.name, child)]
		
		return content
	
	def theme_note(self, form_id, element):
		content = ''
		
		for child_id in ('select', 'title', 'created_date', 'type', 'body'):
			element[child_id](basic_element=True)
			content += element[child_id].render(self.req, current_theme=self)
		
		return content

	def theme_body_text(self, form_id, element):
		return tags.div(_class="note-body")[element.attr('value', '')]