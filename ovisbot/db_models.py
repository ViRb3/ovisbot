import os
import logging

from ovisbot.helpers import escape_md
from ovisbot.locale import _
from pymodm import MongoModel, EmbeddedMongoModel, fields, connect

logger = logging.getLogger(__name__)
connect("mongodb://mongo/ovisdb")


class InstalledCogs(MongoModel):
    name = fields.CharField(required=True)
    enabled = fields.BooleanField(default=True)


class Challenge(EmbeddedMongoModel):
    name = fields.CharField(required=True)
    created_at = fields.DateTimeField(required=True)
    tags = fields.ListField(fields.CharField(), default=[])
    attempted_by = fields.ListField(fields.CharField(), default=[])
    solved_at = fields.DateTimeField(blank=True)
    solved_by = fields.ListField(fields.CharField(), default=[], blank=True)
    notebook_url = fields.CharField(default="", blank=True)
    flag = fields.CharField()


class CTF(MongoModel):
    name = fields.CharField(required=True)
    description = fields.CharField()
    created_at = fields.DateTimeField(required=True)
    finished_at = fields.DateTimeField()
    start_date = fields.DateTimeField()
    finish_date = fields.DateTimeField()
    url = fields.URLField()
    username = fields.CharField()
    password = fields.CharField()
    challenges = fields.EmbeddedDocumentListField(Challenge, default=[])
    reminder = fields.BooleanField(default=False)
    date_for_reminder = fields.DateTimeField()

    def status(self, members_joined_count):
        fmt_str = "%d/%m/%Y-%H:%M:%S"
        start_date_str = self.created_at.strftime(fmt_str)
        end_date_str = (
            self.finished_at.strftime(fmt_str) if self.finished_at else "Live"
        )
        description_str = self.description + "\n" if self.description else ""

        return (
            f":triangular_flag_on_post: **{self.name}** ({members_joined_count} Members joined)\n{description_str}"
            + f"{len(list(filter(lambda x: x.solved_at != None, self.challenges)))} Solved / {len(self.challenges)} Total\n"
            + f"[{start_date_str} - {end_date_str}]\n"
        )

    def credentials(self):
        response = f":busts_in_silhouette: **Username**: {self.username}\n:key: **Password**: {self.password}"
        if self.url is not None:
            response += f"\n\nLogin Here: {self.url}"
        return response

    def challenge_summary(self):
        if not self.challenges:
            return [
                _(
                    "No challenges found. Try adding one with `!ctf addchallenge <name> <category>`"
                )
            ]

        solved_response, unsolved_response = "", ""

        for challenge in self.challenges:
            challenge_details = f'**{escape_md(challenge.name[len(self.name)+1:])}** [{", ".join(challenge.tags)}]'
            if challenge.solved_at:
                solved_response += f':white_check_mark: {challenge_details} Solved by: [{", ".join(challenge.solved_by)}]\n'
            else:
                unsolved_response += f':thinking: {challenge_details} Attempted by: [{escape_md(", ".join(challenge.attempted_by))}]\n'

        summary = (
            f"\\>>> Solved\n{solved_response}" + f"\\>>> Unsolved\n{unsolved_response}"
        )
        return summary

    class Meta:
        collection_name = "ctf"
