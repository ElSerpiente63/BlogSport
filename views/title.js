function title(doc) {
    emit(doc.title, {"first_value":doc.ide, "second_value":doc.content});
}