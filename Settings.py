# -*- coding: ISO-8859-1 -*-
#
# generated by wxGlade 0.9.3 on Thu Jun 27 21:45:40 2019
#

import wx

from Kernel import Module

_ = wx.GetTranslation


# begin wxGlade: dependencies
# end wxGlade

class Settings(wx.Frame, Module):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Preferences.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE | wx.FRAME_TOOL_WINDOW | wx.STAY_ON_TOP
        wx.Frame.__init__(self, *args, **kwds)
        Module.__init__(self)
        self.SetSize((412, 183))

        self.checklist_options = wx.CheckListBox(self, wx.ID_ANY,
                                                 choices=["Invert Mouse Wheel Zoom", "Autoclose Shutdown"])

        self.radio_units = wx.RadioBox(self, wx.ID_ANY, _("Units"),
                                       choices=[_("mm"), _("cm"), _("inch"), _("mils")],
                                       majorDimension=1,
                                       style=wx.RA_SPECIFY_ROWS)

        from wxMeerK40t import supported_languages
        choices = [language_name for language_code, language_name, language_index in supported_languages]
        self.combo_language = wx.ComboBox(self, wx.ID_ANY, choices=choices, style=wx.CB_DROPDOWN)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_RADIOBOX, self.on_radio_units, self.radio_units)
        self.Bind(wx.EVT_COMBOBOX, self.on_combo_language, self.combo_language)
        self.Bind(wx.EVT_CHECKLISTBOX, self.on_checklist_settings, self.checklist_options)
        # end wxGlade
        self.Bind(wx.EVT_CLOSE, self.on_close, self)

    def on_close(self, event):
        self.device.module_instance_remove(self.name)
        event.Skip()  # Call destroy.

    def initialize(self):
        self.device.module_instance_close(self.name)
        self.Show()

        self.device.setting(bool, "mouse_zoom_invert", False)
        self.device.setting(bool, "autoclose_shutdown", True)
        self.device.setting(int, "language", 0)
        self.device.setting(str, "units_name", 'mm')
        self.device.setting(int, "units_marks", 10)
        self.device.setting(int, "units_index", 0)

        if self.device.mouse_zoom_invert:
            self.checklist_options.Check(0, True)
        if self.device.autoclose_shutdown:
            self.checklist_options.Check(1, True)
        self.radio_units.SetSelection(self.device.units_index)
        self.combo_language.SetSelection(self.device.language)

    def shutdown(self):
        self.Close()

    def __set_properties(self):
        # begin wxGlade: Settings.__set_properties
        self.SetTitle(_("Settings"))
        self.radio_units.SetBackgroundColour(wx.Colour(192, 192, 192))
        self.radio_units.SetToolTip(_("Set default units for guides"))
        self.radio_units.SetSelection(0)
        self.combo_language.SetToolTip(_("Select the desired language to use."))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Settings.__do_layout
        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6 = wx.BoxSizer(wx.VERTICAL)
        sizer_5 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, _("Language")), wx.HORIZONTAL)
        sizer_5.Add(self.radio_units, 0, wx.EXPAND, 0)
        sizer_2.Add(self.combo_language, 0, 0, 0)
        sizer_5.Add(sizer_2, 0, wx.EXPAND, 0)
        sizer_1.Add(sizer_5, 1, wx.EXPAND, 0)
        sizer_6.Add(self.checklist_options, 1, wx.EXPAND, 0)
        sizer_1.Add(sizer_6, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

    def on_checklist_settings(self, event):  # wxGlade: Settings.<event_handler>
        self.device.mouse_zoom_invert = self.checklist_options.IsChecked(0)
        self.device.autoclose_shutdown = self.checklist_options.IsChecked(1)

    def on_combo_language(self, event):  # wxGlade: Preferences.<event_handler>
        lang = self.combo_language.GetSelection()
        if lang != -1 and self.device.gui is not None:
            self.device.gui.language_swap(lang)

    def on_radio_units(self, event):  # wxGlade: Preferences.<event_handler>
        if event.Int == 0:
            self.set_mm()
        elif event.Int == 1:
            self.set_cm()
        elif event.Int == 2:
            self.set_inch()
        elif event.Int == 3:
            self.set_mil()

    def set_inch(self):
        p = self.device
        p.units_convert, p.units_name, p.units_marks, p.units_index = (1000.0, "inch", 1, 2)
        p("units", 0)

    def set_mil(self):
        p = self.device
        p.units_convert, p.units_name, p.units_marks, p.units_index = (1.0, "mil", 1000, 3)
        p("units", 0)

    def set_cm(self):
        p = self.device
        p.units_convert, p.units_name, p.units_marks, p.units_index = (393.7, "cm", 1, 1)
        p("units", 0)

    def set_mm(self):
        p = self.device
        p.units_convert, p.units_name, p.units_marks, p.units_index = (39.37, "mm", 10, 0)
        p("units", 0)
