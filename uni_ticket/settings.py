from django.utils.translation import gettext as _

TICKET_ATTACHMENT_FOLDER = 'ticket'
TICKET_MESSAGES_ATTACHMENT_SUBFOLDER = 'messages'
TICKET_TASK_ATTACHMENT_SUBFOLDER = 'task'

TICKET_CONDITIONS_FIELD_ID = 'condizioni_field_id'
TICKET_CONDITIONS_TEXT = _('Ho letto e compreso quanto scritto sopra')

TICKET_SUBJECT_ID = 'ticket_subject'
TICKET_SUBJECT_LABEL = _('Oggetto')
TICKET_SUBJECT_HELP_TEXT = _('Oggetto del Ticket')

TICKET_DESCRIPTION_ID = 'ticket_description'
TICKET_DESCRIPTION_LABEL = _('Descrizione')
TICKET_DESCRIPTION_HELP_TEXT = ('Descrizione del Ticket')

PRIORITY_LEVELS = (
                    ('-2',_('Molto alta')),
                    ('-1',_('Alta')),
                    ('0',_('Normale')),
                    ('1',_('Bassa')),
                    ('2',_('Molto bassa')),
                  )

# If 0 = Unlimited
MAX_DAILY_TICKET_PER_USER = 10

CONTEXT_SIMPLE_USER = _('Utente semplice')
# To change the URLs prefix for every user type
MANAGER_PREFIX = 'Manager'
OPERATOR_PREFIX = 'Operatore'
USER_PREFIX = 'user'

# Do not edit! - START
MANAGEMENT_URL_PREFIX = {'manager': MANAGER_PREFIX,
                         'operator': OPERATOR_PREFIX,
                         'user': USER_PREFIX}
# Do not edit! - END

# Competenza sul ticket abbandonata
NO_MORE_COMPETENCE_OVER_TICKET = _("Nessuna competenza sul ticket")
# Accesso sul ticket in sola lettura
READONLY_COMPETENCE_OVER_TICKET = _("Hai accesso al ticket in sola lettura")

# E-mail messages
MSG_HEADER = _("""Gentile {user},
questo messaggio è stato inviato da {hostname}.
Per favore non rispondere a questa email.

-------------------

""")

MSG_FOOTER = _("""

-------------------

Per problemi tecnici contatta il nostro staff.
Cordiali saluti.
""")

NEW_TICKET_CREATED = _("""Il ticket "{ticket}" è stato creato correttamente.

Dati inseriti:
{data}

Files:
{files}""")

TICKET_UPDATED = _("""Il ticket "{ticket}" è stato aggiornato con il seguente messaggio:

{message}""")

USER_TICKET_MESSAGE = _("""Hai {status} un messaggio per il ticket \"{ticket}\"""")

TICKET_DELETED = _("""Il ticket "{ticket}" è stato eliminato correttamente.""")

SUMMARY_USER_EMAIL = _("""Il seguente ticket {event msg}:

{ticket}""")

SUMMARY_EMPLOYEE_EMAIL = _("""Hai {open_ticket_number} tickets da gestire.

{tickets_per_office}""")

# Old english version
NEW_TICKET_UPDATE_OLD_EN = _("Dear {user},"
                      "you have successfully {status} the ticket:"
                      ""
                      "{ticket}"
                      ""
                      "This message was sent to you by {hostname}."
                      "Please do not reply to this email.")

USER_TICKET_MESSAGE_OLD_EN = _("Dear {user},"
                       "you have successfully {status} a message for ticket:"
                       ""
                       "{ticket}"
                       ""
                       "This message was sent to you by {hostname}."
                       "Please do not reply to this email.")

TICKET_UPDATED_OLD_EN = _("Dear {user},"
                   "the ticket:"
                   ""
                   "{ticket}"
                   ""
                   "has been updated with the message:"
                   ""
                   "{message}."
                   ""
                   "This message was sent to you by {hostname}."
                   "Please do not reply to this email.")

SUMMARY_USER_EMAIL_OLD_EN = _("Dear {user},"
                       "the following ticket {event_msg}:"
                       ""
                       "{ticket}"
                       ""
                       "This message was sent to you by {hostname}."
                       "Please do not reply to this email.")

SUMMARY_EMPLOYEE_EMAIL_OLD_EN = _("Dear {user},"
                           "You have {open_ticket_number} tickets to manage."
                           ""
                           "{tickets_per_office}"
                           ""
                           "This message was sent to you by {hostname}."
                           "Please do not reply to this email.")
