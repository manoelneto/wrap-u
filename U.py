#-*- coding: utf-8 -*-
import sublime_plugin
import re


class UCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sels = self.view.sel()
        edit = self.view.begin_edit()
        u_re = re.compile(r'^u\(([^\)]+)\)$')

        for sel in sels:
            content = self.view.substr(sel)
            has_u = u_re.search(content)
            if has_u:
                new_content = has_u.group(1)
            else:
                new_content = 'u(%s)' % (content,)
            self.view.replace(edit, sel, new_content)
        self.view.end_edit(edit)
