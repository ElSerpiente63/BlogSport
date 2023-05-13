function register (doc) {
    if (doc && doc.username){
      emit(doc.username);
    }
  }