from rest_framework import serializers

from core.models import Post, Commentaries


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "title",
            "time_to_cook",
            "count",
            "body",
            "slug",
            "cat",
            "dish",
        )
        depth = 1

    def validate(self, attrs):
        bad_words = ["apple", "orange", "black", "white"]
        title_words = attrs["title"].split()
        body_words = attrs["body"].split()

        for word in title_words:
            if word in bad_words:
                raise serializers.ValidationError(
                    {"title": f"Содержит недопустые слово: {word}"}
                )

        for word in body_words:
            if word in bad_words:
                raise serializers.ValidationError(
                    {"body": f"Содержит недопустые слово: {word}"}
                )

        return attrs


class CommentariesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commentaries
        fields = (
            "author",
            "comment",
        )
        depth = 1
