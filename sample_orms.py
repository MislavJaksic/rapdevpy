class /alliances/(Base):
    __tablename__ = /alliances/


    def __repr__(self):
        return ''.format()

class /alliances/{alliance_id}/(Base):
    __tablename__ = /alliances/{alliance_id}/

    creator_corporation_id = Column(Integer)
    creator_id = Column(Integer)
    date_founded = Column(DateTime)
    executor_corporation_id = Column(Integer)
    faction_id = Column(Integer)
    name = Column(String)
    ticker = Column(String)

    def __repr__(self):
        return 'creator_corporation_id={}, creator_id={}, date_founded={}, executor_corporation_id={}, faction_id={}, name={}, ticker={}'.format(self.creator_corporation_id, self.creator_id, self.date_founded, self.executor_corporation_id, self.faction_id, self.name, self.ticker)

class /alliances/{alliance_id}/contacts/(Base):
    __tablename__ = /alliances/{alliance_id}/contacts/

    contact_id = Column(Integer)
    contact_type = Column(String)
    label_ids = Column(Array)
    standing = Column(Float)

    def __repr__(self):
        return 'contact_id={}, contact_type={}, label_ids={}, standing={}'.format(self.contact_id, self.contact_type, self.label_ids, self.standing)

class /alliances/{alliance_id}/contacts/labels/(Base):
    __tablename__ = /alliances/{alliance_id}/contacts/labels/

    label_id = Column(Integer)
    label_name = Column(String)

    def __repr__(self):
        return 'label_id={}, label_name={}'.format(self.label_id, self.label_name)

class /alliances/{alliance_id}/corporations/(Base):
    __tablename__ = /alliances/{alliance_id}/corporations/


    def __repr__(self):
        return ''.format()

class /alliances/{alliance_id}/icons/(Base):
    __tablename__ = /alliances/{alliance_id}/icons/

    px128x128 = Column(String)
    px64x64 = Column(String)

    def __repr__(self):
        return 'px128x128={}, px64x64={}'.format(self.px128x128, self.px64x64)

class /characters/affiliation/(Base):
    __tablename__ = /characters/affiliation/

    alliance_id = Column(Integer)
    character_id = Column(Integer)
    corporation_id = Column(Integer)
    faction_id = Column(Integer)

    def __repr__(self):
        return 'alliance_id={}, character_id={}, corporation_id={}, faction_id={}'.format(self.alliance_id, self.character_id, self.corporation_id, self.faction_id)

class /characters/{character_id}/(Base):
    __tablename__ = /characters/{character_id}/

    alliance_id = Column(Integer)
    ancestry_id = Column(Integer)
    birthday = Column(DateTime)
    bloodline_id = Column(Integer)
    corporation_id = Column(Integer)
    description = Column(String)
    faction_id = Column(Integer)
    gender = Column(String)
    name = Column(String)
    race_id = Column(Integer)
    security_status = Column(Float)
    title = Column(String)

    def __repr__(self):
        return 'alliance_id={}, ancestry_id={}, birthday={}, bloodline_id={}, corporation_id={}, description={}, faction_id={}, gender={}, name={}, race_id={}, security_status={}, title={}'.format(self.alliance_id, self.ancestry_id, self.birthday, self.bloodline_id, self.corporation_id, self.description, self.faction_id, self.gender, self.name, self.race_id, self.security_status, self.title)

class /characters/{character_id}/agents_research/(Base):
    __tablename__ = /characters/{character_id}/agents_research/

    agent_id = Column(Integer)
    points_per_day = Column(Float)
    remainder_points = Column(Float)
    skill_type_id = Column(Integer)
    started_at = Column(DateTime)

    def __repr__(self):
        return 'agent_id={}, points_per_day={}, remainder_points={}, skill_type_id={}, started_at={}'.format(self.agent_id, self.points_per_day, self.remainder_points, self.skill_type_id, self.started_at)

class /characters/{character_id}/assets/(Base):
    __tablename__ = /characters/{character_id}/assets/

    is_blueprint_copy = Column(Boolean)
    is_singleton = Column(Boolean)
    item_id = Column(Integer)
    location_flag = Column(String)
    location_id = Column(Integer)
    location_type = Column(String)
    quantity = Column(Integer)
    type_id = Column(Integer)

    def __repr__(self):
        return 'is_blueprint_copy={}, is_singleton={}, item_id={}, location_flag={}, location_id={}, location_type={}, quantity={}, type_id={}'.format(self.is_blueprint_copy, self.is_singleton, self.item_id, self.location_flag, self.location_id, self.location_type, self.quantity, self.type_id)

class /characters/{character_id}/assets/locations/(Base):
    __tablename__ = /characters/{character_id}/assets/locations/

    item_id = Column(Integer)
    position = Column(Object)

    def __repr__(self):
        return 'item_id={}, position={}'.format(self.item_id, self.position)

class /characters/{character_id}/assets/names/(Base):
    __tablename__ = /characters/{character_id}/assets/names/

    item_id = Column(Integer)
    name = Column(String)

    def __repr__(self):
        return 'item_id={}, name={}'.format(self.item_id, self.name)

class /characters/{character_id}/attributes/(Base):
    __tablename__ = /characters/{character_id}/attributes/

    accrued_remap_cooldown_date = Column(DateTime)
    bonus_remaps = Column(Integer)
    charisma = Column(Integer)
    intelligence = Column(Integer)
    last_remap_date = Column(DateTime)
    memory = Column(Integer)
    perception = Column(Integer)
    willpower = Column(Integer)

    def __repr__(self):
        return 'accrued_remap_cooldown_date={}, bonus_remaps={}, charisma={}, intelligence={}, last_remap_date={}, memory={}, perception={}, willpower={}'.format(self.accrued_remap_cooldown_date, self.bonus_remaps, self.charisma, self.intelligence, self.last_remap_date, self.memory, self.perception, self.willpower)

class /characters/{character_id}/blueprints/(Base):
    __tablename__ = /characters/{character_id}/blueprints/

    item_id = Column(Integer)
    location_flag = Column(String)
    location_id = Column(Integer)
    material_efficiency = Column(Integer)
    quantity = Column(Integer)
    runs = Column(Integer)
    time_efficiency = Column(Integer)
    type_id = Column(Integer)

    def __repr__(self):
        return 'item_id={}, location_flag={}, location_id={}, material_efficiency={}, quantity={}, runs={}, time_efficiency={}, type_id={}'.format(self.item_id, self.location_flag, self.location_id, self.material_efficiency, self.quantity, self.runs, self.time_efficiency, self.type_id)

class /characters/{character_id}/bookmarks/(Base):
    __tablename__ = /characters/{character_id}/bookmarks/

    bookmark_id = Column(Integer)
    coordinates = Column(Object)
    created = Column(DateTime)
    creator_id = Column(Integer)
    folder_id = Column(Integer)
    item = Column(Object)
    label = Column(String)
    location_id = Column(Integer)
    notes = Column(String)

    def __repr__(self):
        return 'bookmark_id={}, coordinates={}, created={}, creator_id={}, folder_id={}, item={}, label={}, location_id={}, notes={}'.format(self.bookmark_id, self.coordinates, self.created, self.creator_id, self.folder_id, self.item, self.label, self.location_id, self.notes)

class /characters/{character_id}/bookmarks/folders/(Base):
    __tablename__ = /characters/{character_id}/bookmarks/folders/

    folder_id = Column(Integer)
    name = Column(String)

    def __repr__(self):
        return 'folder_id={}, name={}'.format(self.folder_id, self.name)

class /characters/{character_id}/calendar/(Base):
    __tablename__ = /characters/{character_id}/calendar/

    event_date = Column(DateTime)
    event_id = Column(Integer)
    event_response = Column(String)
    importance = Column(Integer)
    title = Column(String)

    def __repr__(self):
        return 'event_date={}, event_id={}, event_response={}, importance={}, title={}'.format(self.event_date, self.event_id, self.event_response, self.importance, self.title)

class /characters/{character_id}/calendar/{event_id}/(Base):
    __tablename__ = /characters/{character_id}/calendar/{event_id}/

    date = Column(DateTime)
    duration = Column(Integer)
    event_id = Column(Integer)
    importance = Column(Integer)
    owner_id = Column(Integer)
    owner_name = Column(String)
    owner_type = Column(String)
    response = Column(String)
    text = Column(String)
    title = Column(String)

    def __repr__(self):
        return 'date={}, duration={}, event_id={}, importance={}, owner_id={}, owner_name={}, owner_type={}, response={}, text={}, title={}'.format(self.date, self.duration, self.event_id, self.importance, self.owner_id, self.owner_name, self.owner_type, self.response, self.text, self.title)

class /characters/{character_id}/calendar/{event_id}/attendees/(Base):
    __tablename__ = /characters/{character_id}/calendar/{event_id}/attendees/

    character_id = Column(Integer)
    event_response = Column(String)

    def __repr__(self):
        return 'character_id={}, event_response={}'.format(self.character_id, self.event_response)

class /characters/{character_id}/clones/(Base):
    __tablename__ = /characters/{character_id}/clones/

    home_location = Column(Object)
    jump_clones = Column(Array)
    last_clone_jump_date = Column(DateTime)
    last_station_change_date = Column(DateTime)

    def __repr__(self):
        return 'home_location={}, jump_clones={}, last_clone_jump_date={}, last_station_change_date={}'.format(self.home_location, self.jump_clones, self.last_clone_jump_date, self.last_station_change_date)

class /characters/{character_id}/contacts/(Base):
    __tablename__ = /characters/{character_id}/contacts/

    contact_id = Column(Integer)
    contact_type = Column(String)
    is_blocked = Column(Boolean)
    is_watched = Column(Boolean)
    label_ids = Column(Array)
    standing = Column(Float)

    def __repr__(self):
        return 'contact_id={}, contact_type={}, is_blocked={}, is_watched={}, label_ids={}, standing={}'.format(self.contact_id, self.contact_type, self.is_blocked, self.is_watched, self.label_ids, self.standing)

class /characters/{character_id}/contacts/labels/(Base):
    __tablename__ = /characters/{character_id}/contacts/labels/

    label_id = Column(Integer)
    label_name = Column(String)

    def __repr__(self):
        return 'label_id={}, label_name={}'.format(self.label_id, self.label_name)

class /characters/{character_id}/contracts/(Base):
    __tablename__ = /characters/{character_id}/contracts/

    acceptor_id = Column(Integer)
    assignee_id = Column(Integer)
    availability = Column(String)
    buyout = Column(Float)
    collateral = Column(Float)
    contract_id = Column(Integer)
    date_accepted = Column(DateTime)
    date_completed = Column(DateTime)
    date_expired = Column(DateTime)
    date_issued = Column(DateTime)
    days_to_complete = Column(Integer)
    end_location_id = Column(Integer)
    for_corporation = Column(Boolean)
    issuer_corporation_id = Column(Integer)
    issuer_id = Column(Integer)
    price = Column(Float)
    reward = Column(Float)
    start_location_id = Column(Integer)
    status = Column(String)
    title = Column(String)
    type = Column(String)
    volume = Column(Float)

    def __repr__(self):
        return 'acceptor_id={}, assignee_id={}, availability={}, buyout={}, collateral={}, contract_id={}, date_accepted={}, date_completed={}, date_expired={}, date_issued={}, days_to_complete={}, end_location_id={}, for_corporation={}, issuer_corporation_id={}, issuer_id={}, price={}, reward={}, start_location_id={}, status={}, title={}, type={}, volume={}'.format(self.acceptor_id, self.assignee_id, self.availability, self.buyout, self.collateral, self.contract_id, self.date_accepted, self.date_completed, self.date_expired, self.date_issued, self.days_to_complete, self.end_location_id, self.for_corporation, self.issuer_corporation_id, self.issuer_id, self.price, self.reward, self.start_location_id, self.status, self.title, self.type, self.volume)

class /characters/{character_id}/contracts/{contract_id}/bids/(Base):
    __tablename__ = /characters/{character_id}/contracts/{contract_id}/bids/

    amount = Column(Float)
    bid_id = Column(Integer)
    bidder_id = Column(Integer)
    date_bid = Column(DateTime)

    def __repr__(self):
        return 'amount={}, bid_id={}, bidder_id={}, date_bid={}'.format(self.amount, self.bid_id, self.bidder_id, self.date_bid)

class /characters/{character_id}/contracts/{contract_id}/items/(Base):
    __tablename__ = /characters/{character_id}/contracts/{contract_id}/items/

    is_included = Column(Boolean)
    is_singleton = Column(Boolean)
    quantity = Column(Integer)
    raw_quantity = Column(Integer)
    record_id = Column(Integer)
    type_id = Column(Integer)

    def __repr__(self):
        return 'is_included={}, is_singleton={}, quantity={}, raw_quantity={}, record_id={}, type_id={}'.format(self.is_included, self.is_singleton, self.quantity, self.raw_quantity, self.record_id, self.type_id)

class /characters/{character_id}/corporationhistory/(Base):
    __tablename__ = /characters/{character_id}/corporationhistory/

    corporation_id = Column(Integer)
    is_deleted = Column(Boolean)
    record_id = Column(Integer)
    start_date = Column(DateTime)

    def __repr__(self):
        return 'corporation_id={}, is_deleted={}, record_id={}, start_date={}'.format(self.corporation_id, self.is_deleted, self.record_id, self.start_date)

class /characters/{character_id}/fatigue/(Base):
    __tablename__ = /characters/{character_id}/fatigue/

    jump_fatigue_expire_date = Column(DateTime)
    last_jump_date = Column(DateTime)
    last_update_date = Column(DateTime)

    def __repr__(self):
        return 'jump_fatigue_expire_date={}, last_jump_date={}, last_update_date={}'.format(self.jump_fatigue_expire_date, self.last_jump_date, self.last_update_date)

class /characters/{character_id}/fittings/(Base):
    __tablename__ = /characters/{character_id}/fittings/

    description = Column(String)
    fitting_id = Column(Integer)
    items = Column(Array)
    name = Column(String)
    ship_type_id = Column(Integer)

    def __repr__(self):
        return 'description={}, fitting_id={}, items={}, name={}, ship_type_id={}'.format(self.description, self.fitting_id, self.items, self.name, self.ship_type_id)

class /characters/{character_id}/fittings/{fitting_id}/(Base):
    __tablename__ = /characters/{character_id}/fittings/{fitting_id}/

    description = Column(String)
    fitting_id = Column(Integer)
    items = Column(Array)
    name = Column(String)
    ship_type_id = Column(Integer)

    def __repr__(self):
        return 'description={}, fitting_id={}, items={}, name={}, ship_type_id={}'.format(self.description, self.fitting_id, self.items, self.name, self.ship_type_id)

class /characters/{character_id}/fleet/(Base):
    __tablename__ = /characters/{character_id}/fleet/

    fleet_id = Column(Integer)
    role = Column(String)
    squad_id = Column(Integer)
    wing_id = Column(Integer)

    def __repr__(self):
        return 'fleet_id={}, role={}, squad_id={}, wing_id={}'.format(self.fleet_id, self.role, self.squad_id, self.wing_id)

class /characters/{character_id}/fw/stats/(Base):
    __tablename__ = /characters/{character_id}/fw/stats/

    current_rank = Column(Integer)
    enlisted_on = Column(DateTime)
    faction_id = Column(Integer)
    highest_rank = Column(Integer)
    kills = Column(Object)
    victory_points = Column(Object)

    def __repr__(self):
        return 'current_rank={}, enlisted_on={}, faction_id={}, highest_rank={}, kills={}, victory_points={}'.format(self.current_rank, self.enlisted_on, self.faction_id, self.highest_rank, self.kills, self.victory_points)

class /characters/{character_id}/implants/(Base):
    __tablename__ = /characters/{character_id}/implants/


    def __repr__(self):
        return ''.format()

class /characters/{character_id}/industry/jobs/(Base):
    __tablename__ = /characters/{character_id}/industry/jobs/

    activity_id = Column(Integer)
    blueprint_id = Column(Integer)
    blueprint_location_id = Column(Integer)
    blueprint_type_id = Column(Integer)
    completed_character_id = Column(Integer)
    completed_date = Column(DateTime)
    cost = Column(Float)
    duration = Column(Integer)
    end_date = Column(DateTime)
    facility_id = Column(Integer)
    installer_id = Column(Integer)
    job_id = Column(Integer)
    licensed_runs = Column(Integer)
    output_location_id = Column(Integer)
    pause_date = Column(DateTime)
    probability = Column(Float)
    product_type_id = Column(Integer)
    runs = Column(Integer)
    start_date = Column(DateTime)
    station_id = Column(Integer)
    status = Column(String)
    successful_runs = Column(Integer)

    def __repr__(self):
        return 'activity_id={}, blueprint_id={}, blueprint_location_id={}, blueprint_type_id={}, completed_character_id={}, completed_date={}, cost={}, duration={}, end_date={}, facility_id={}, installer_id={}, job_id={}, licensed_runs={}, output_location_id={}, pause_date={}, probability={}, product_type_id={}, runs={}, start_date={}, station_id={}, status={}, successful_runs={}'.format(self.activity_id, self.blueprint_id, self.blueprint_location_id, self.blueprint_type_id, self.completed_character_id, self.completed_date, self.cost, self.duration, self.end_date, self.facility_id, self.installer_id, self.job_id, self.licensed_runs, self.output_location_id, self.pause_date, self.probability, self.product_type_id, self.runs, self.start_date, self.station_id, self.status, self.successful_runs)

class /characters/{character_id}/killmails/recent/(Base):
    __tablename__ = /characters/{character_id}/killmails/recent/

    killmail_hash = Column(String)
    killmail_id = Column(Integer)

    def __repr__(self):
        return 'killmail_hash={}, killmail_id={}'.format(self.killmail_hash, self.killmail_id)

class /characters/{character_id}/location/(Base):
    __tablename__ = /characters/{character_id}/location/

    solar_system_id = Column(Integer)
    station_id = Column(Integer)
    structure_id = Column(Integer)

    def __repr__(self):
        return 'solar_system_id={}, station_id={}, structure_id={}'.format(self.solar_system_id, self.station_id, self.structure_id)

class /characters/{character_id}/loyalty/points/(Base):
    __tablename__ = /characters/{character_id}/loyalty/points/

    corporation_id = Column(Integer)
    loyalty_points = Column(Integer)

    def __repr__(self):
        return 'corporation_id={}, loyalty_points={}'.format(self.corporation_id, self.loyalty_points)

class /characters/{character_id}/mail/(Base):
    __tablename__ = /characters/{character_id}/mail/

    from = Column(Integer)
    is_read = Column(Boolean)
    labels = Column(Array)
    mail_id = Column(Integer)
    recipients = Column(Array)
    subject = Column(String)
    timestamp = Column(DateTime)

    def __repr__(self):
        return 'from={}, is_read={}, labels={}, mail_id={}, recipients={}, subject={}, timestamp={}'.format(self.from, self.is_read, self.labels, self.mail_id, self.recipients, self.subject, self.timestamp)

class /characters/{character_id}/mail/labels/(Base):
    __tablename__ = /characters/{character_id}/mail/labels/

    labels = Column(Array)
    total_unread_count = Column(Integer)

    def __repr__(self):
        return 'labels={}, total_unread_count={}'.format(self.labels, self.total_unread_count)

class /characters/{character_id}/mail/labels/{label_id}/(Base):
    __tablename__ = /characters/{character_id}/mail/labels/{label_id}/

    labels = Column(Array)
    total_unread_count = Column(Integer)

    def __repr__(self):
        return 'labels={}, total_unread_count={}'.format(self.labels, self.total_unread_count)

class /characters/{character_id}/mail/lists/(Base):
    __tablename__ = /characters/{character_id}/mail/lists/

    mailing_list_id = Column(Integer)
    name = Column(String)

    def __repr__(self):
        return 'mailing_list_id={}, name={}'.format(self.mailing_list_id, self.name)

class /characters/{character_id}/mail/{mail_id}/(Base):
    __tablename__ = /characters/{character_id}/mail/{mail_id}/

    body = Column(String)
    from = Column(Integer)
    labels = Column(Array)
    read = Column(Boolean)
    recipients = Column(Array)
    subject = Column(String)
    timestamp = Column(DateTime)

    def __repr__(self):
        return 'body={}, from={}, labels={}, read={}, recipients={}, subject={}, timestamp={}'.format(self.body, self.from, self.labels, self.read, self.recipients, self.subject, self.timestamp)

class /characters/{character_id}/medals/(Base):
    __tablename__ = /characters/{character_id}/medals/

    corporation_id = Column(Integer)
    date = Column(DateTime)
    description = Column(String)
    graphics = Column(Array)
    issuer_id = Column(Integer)
    medal_id = Column(Integer)
    reason = Column(String)
    status = Column(String)
    title = Column(String)

    def __repr__(self):
        return 'corporation_id={}, date={}, description={}, graphics={}, issuer_id={}, medal_id={}, reason={}, status={}, title={}'.format(self.corporation_id, self.date, self.description, self.graphics, self.issuer_id, self.medal_id, self.reason, self.status, self.title)

class /characters/{character_id}/mining/(Base):
    __tablename__ = /characters/{character_id}/mining/

    date = Column(Date)
    quantity = Column(Integer)
    solar_system_id = Column(Integer)
    type_id = Column(Integer)

    def __repr__(self):
        return 'date={}, quantity={}, solar_system_id={}, type_id={}'.format(self.date, self.quantity, self.solar_system_id, self.type_id)

class /characters/{character_id}/notifications/(Base):
    __tablename__ = /characters/{character_id}/notifications/

    is_read = Column(Boolean)
    notification_id = Column(Integer)
    sender_id = Column(Integer)
    sender_type = Column(String)
    text = Column(String)
    timestamp = Column(DateTime)
    type = Column(String)

    def __repr__(self):
        return 'is_read={}, notification_id={}, sender_id={}, sender_type={}, text={}, timestamp={}, type={}'.format(self.is_read, self.notification_id, self.sender_id, self.sender_type, self.text, self.timestamp, self.type)

class /characters/{character_id}/notifications/contacts/(Base):
    __tablename__ = /characters/{character_id}/notifications/contacts/

    message = Column(String)
    notification_id = Column(Integer)
    send_date = Column(DateTime)
    sender_character_id = Column(Integer)
    standing_level = Column(Float)

    def __repr__(self):
        return 'message={}, notification_id={}, send_date={}, sender_character_id={}, standing_level={}'.format(self.message, self.notification_id, self.send_date, self.sender_character_id, self.standing_level)

class /characters/{character_id}/online/(Base):
    __tablename__ = /characters/{character_id}/online/

    last_login = Column(DateTime)
    last_logout = Column(DateTime)
    logins = Column(Integer)
    online = Column(Boolean)

    def __repr__(self):
        return 'last_login={}, last_logout={}, logins={}, online={}'.format(self.last_login, self.last_logout, self.logins, self.online)

class /characters/{character_id}/opportunities/(Base):
    __tablename__ = /characters/{character_id}/opportunities/

    completed_at = Column(DateTime)
    task_id = Column(Integer)

    def __repr__(self):
        return 'completed_at={}, task_id={}'.format(self.completed_at, self.task_id)

class /characters/{character_id}/orders/(Base):
    __tablename__ = /characters/{character_id}/orders/

    duration = Column(Integer)
    escrow = Column(Float)
    is_buy_order = Column(Boolean)
    is_corporation = Column(Boolean)
    issued = Column(DateTime)
    location_id = Column(Integer)
    min_volume = Column(Integer)
    order_id = Column(Integer)
    price = Column(Float)
    range = Column(String)
    region_id = Column(Integer)
    type_id = Column(Integer)
    volume_remain = Column(Integer)
    volume_total = Column(Integer)

    def __repr__(self):
        return 'duration={}, escrow={}, is_buy_order={}, is_corporation={}, issued={}, location_id={}, min_volume={}, order_id={}, price={}, range={}, region_id={}, type_id={}, volume_remain={}, volume_total={}'.format(self.duration, self.escrow, self.is_buy_order, self.is_corporation, self.issued, self.location_id, self.min_volume, self.order_id, self.price, self.range, self.region_id, self.type_id, self.volume_remain, self.volume_total)

class /characters/{character_id}/orders/history/(Base):
    __tablename__ = /characters/{character_id}/orders/history/

    duration = Column(Integer)
    escrow = Column(Float)
    is_buy_order = Column(Boolean)
    is_corporation = Column(Boolean)
    issued = Column(DateTime)
    location_id = Column(Integer)
    min_volume = Column(Integer)
    order_id = Column(Integer)
    price = Column(Float)
    range = Column(String)
    region_id = Column(Integer)
    state = Column(String)
    type_id = Column(Integer)
    volume_remain = Column(Integer)
    volume_total = Column(Integer)

    def __repr__(self):
        return 'duration={}, escrow={}, is_buy_order={}, is_corporation={}, issued={}, location_id={}, min_volume={}, order_id={}, price={}, range={}, region_id={}, state={}, type_id={}, volume_remain={}, volume_total={}'.format(self.duration, self.escrow, self.is_buy_order, self.is_corporation, self.issued, self.location_id, self.min_volume, self.order_id, self.price, self.range, self.region_id, self.state, self.type_id, self.volume_remain, self.volume_total)

class /characters/{character_id}/planets/(Base):
    __tablename__ = /characters/{character_id}/planets/

    last_update = Column(DateTime)
    num_pins = Column(Integer)
    owner_id = Column(Integer)
    planet_id = Column(Integer)
    planet_type = Column(String)
    solar_system_id = Column(Integer)
    upgrade_level = Column(Integer)

    def __repr__(self):
        return 'last_update={}, num_pins={}, owner_id={}, planet_id={}, planet_type={}, solar_system_id={}, upgrade_level={}'.format(self.last_update, self.num_pins, self.owner_id, self.planet_id, self.planet_type, self.solar_system_id, self.upgrade_level)

class /characters/{character_id}/planets/{planet_id}/(Base):
    __tablename__ = /characters/{character_id}/planets/{planet_id}/

    links = Column(Array)
    pins = Column(Array)
    routes = Column(Array)

    def __repr__(self):
        return 'links={}, pins={}, routes={}'.format(self.links, self.pins, self.routes)

class /characters/{character_id}/portrait/(Base):
    __tablename__ = /characters/{character_id}/portrait/

    px128x128 = Column(String)
    px256x256 = Column(String)
    px512x512 = Column(String)
    px64x64 = Column(String)

    def __repr__(self):
        return 'px128x128={}, px256x256={}, px512x512={}, px64x64={}'.format(self.px128x128, self.px256x256, self.px512x512, self.px64x64)

class /characters/{character_id}/roles/(Base):
    __tablename__ = /characters/{character_id}/roles/

    roles = Column(Array)
    roles_at_base = Column(Array)
    roles_at_hq = Column(Array)
    roles_at_other = Column(Array)

    def __repr__(self):
        return 'roles={}, roles_at_base={}, roles_at_hq={}, roles_at_other={}'.format(self.roles, self.roles_at_base, self.roles_at_hq, self.roles_at_other)

class /characters/{character_id}/search/(Base):
    __tablename__ = /characters/{character_id}/search/

    agent = Column(Array)
    alliance = Column(Array)
    character = Column(Array)
    constellation = Column(Array)
    corporation = Column(Array)
    faction = Column(Array)
    inventory_type = Column(Array)
    region = Column(Array)
    solar_system = Column(Array)
    station = Column(Array)
    structure = Column(Array)

    def __repr__(self):
        return 'agent={}, alliance={}, character={}, constellation={}, corporation={}, faction={}, inventory_type={}, region={}, solar_system={}, station={}, structure={}'.format(self.agent, self.alliance, self.character, self.constellation, self.corporation, self.faction, self.inventory_type, self.region, self.solar_system, self.station, self.structure)

class /characters/{character_id}/ship/(Base):
    __tablename__ = /characters/{character_id}/ship/

    ship_item_id = Column(Integer)
    ship_name = Column(String)
    ship_type_id = Column(Integer)

    def __repr__(self):
        return 'ship_item_id={}, ship_name={}, ship_type_id={}'.format(self.ship_item_id, self.ship_name, self.ship_type_id)

class /characters/{character_id}/skillqueue/(Base):
    __tablename__ = /characters/{character_id}/skillqueue/

    finish_date = Column(DateTime)
    finished_level = Column(Integer)
    level_end_sp = Column(Integer)
    level_start_sp = Column(Integer)
    queue_position = Column(Integer)
    skill_id = Column(Integer)
    start_date = Column(DateTime)
    training_start_sp = Column(Integer)

    def __repr__(self):
        return 'finish_date={}, finished_level={}, level_end_sp={}, level_start_sp={}, queue_position={}, skill_id={}, start_date={}, training_start_sp={}'.format(self.finish_date, self.finished_level, self.level_end_sp, self.level_start_sp, self.queue_position, self.skill_id, self.start_date, self.training_start_sp)

class /characters/{character_id}/skills/(Base):
    __tablename__ = /characters/{character_id}/skills/

    skills = Column(Array)
    total_sp = Column(Integer)
    unallocated_sp = Column(Integer)

    def __repr__(self):
        return 'skills={}, total_sp={}, unallocated_sp={}'.format(self.skills, self.total_sp, self.unallocated_sp)

class /characters/{character_id}/standings/(Base):
    __tablename__ = /characters/{character_id}/standings/

    from_id = Column(Integer)
    from_type = Column(String)
    standing = Column(Float)

    def __repr__(self):
        return 'from_id={}, from_type={}, standing={}'.format(self.from_id, self.from_type, self.standing)

class /characters/{character_id}/titles/(Base):
    __tablename__ = /characters/{character_id}/titles/

    name = Column(String)
    title_id = Column(Integer)

    def __repr__(self):
        return 'name={}, title_id={}'.format(self.name, self.title_id)

class /characters/{character_id}/wallet/(Base):
    __tablename__ = /characters/{character_id}/wallet/


    def __repr__(self):
        return ''.format()

class /characters/{character_id}/wallet/journal/(Base):
    __tablename__ = /characters/{character_id}/wallet/journal/

    amount = Column(Float)
    balance = Column(Float)
    context_id = Column(Integer)
    context_id_type = Column(String)
    date = Column(DateTime)
    description = Column(String)
    first_party_id = Column(Integer)
    id = Column(Integer)
    reason = Column(String)
    ref_type = Column(String)
    second_party_id = Column(Integer)
    tax = Column(Float)
    tax_receiver_id = Column(Integer)

    def __repr__(self):
        return 'amount={}, balance={}, context_id={}, context_id_type={}, date={}, description={}, first_party_id={}, id={}, reason={}, ref_type={}, second_party_id={}, tax={}, tax_receiver_id={}'.format(self.amount, self.balance, self.context_id, self.context_id_type, self.date, self.description, self.first_party_id, self.id, self.reason, self.ref_type, self.second_party_id, self.tax, self.tax_receiver_id)

class /characters/{character_id}/wallet/transactions/(Base):
    __tablename__ = /characters/{character_id}/wallet/transactions/

    client_id = Column(Integer)
    date = Column(DateTime)
    is_buy = Column(Boolean)
    is_personal = Column(Boolean)
    journal_ref_id = Column(Integer)
    location_id = Column(Integer)
    quantity = Column(Integer)
    transaction_id = Column(Integer)
    type_id = Column(Integer)
    unit_price = Column(Float)

    def __repr__(self):
        return 'client_id={}, date={}, is_buy={}, is_personal={}, journal_ref_id={}, location_id={}, quantity={}, transaction_id={}, type_id={}, unit_price={}'.format(self.client_id, self.date, self.is_buy, self.is_personal, self.journal_ref_id, self.location_id, self.quantity, self.transaction_id, self.type_id, self.unit_price)

class /contracts/public/bids/{contract_id}/(Base):
    __tablename__ = /contracts/public/bids/{contract_id}/

    amount = Column(Float)
    bid_id = Column(Integer)
    date_bid = Column(DateTime)

    def __repr__(self):
        return 'amount={}, bid_id={}, date_bid={}'.format(self.amount, self.bid_id, self.date_bid)

class /contracts/public/items/{contract_id}/(Base):
    __tablename__ = /contracts/public/items/{contract_id}/

    is_blueprint_copy = Column(Boolean)
    is_included = Column(Boolean)
    item_id = Column(Integer)
    material_efficiency = Column(Integer)
    quantity = Column(Integer)
    record_id = Column(Integer)
    runs = Column(Integer)
    time_efficiency = Column(Integer)
    type_id = Column(Integer)

    def __repr__(self):
        return 'is_blueprint_copy={}, is_included={}, item_id={}, material_efficiency={}, quantity={}, record_id={}, runs={}, time_efficiency={}, type_id={}'.format(self.is_blueprint_copy, self.is_included, self.item_id, self.material_efficiency, self.quantity, self.record_id, self.runs, self.time_efficiency, self.type_id)

class /contracts/public/{region_id}/(Base):
    __tablename__ = /contracts/public/{region_id}/

    buyout = Column(Float)
    collateral = Column(Float)
    contract_id = Column(Integer)
    date_expired = Column(DateTime)
    date_issued = Column(DateTime)
    days_to_complete = Column(Integer)
    end_location_id = Column(Integer)
    for_corporation = Column(Boolean)
    issuer_corporation_id = Column(Integer)
    issuer_id = Column(Integer)
    price = Column(Float)
    reward = Column(Float)
    start_location_id = Column(Integer)
    title = Column(String)
    type = Column(String)
    volume = Column(Float)

    def __repr__(self):
        return 'buyout={}, collateral={}, contract_id={}, date_expired={}, date_issued={}, days_to_complete={}, end_location_id={}, for_corporation={}, issuer_corporation_id={}, issuer_id={}, price={}, reward={}, start_location_id={}, title={}, type={}, volume={}'.format(self.buyout, self.collateral, self.contract_id, self.date_expired, self.date_issued, self.days_to_complete, self.end_location_id, self.for_corporation, self.issuer_corporation_id, self.issuer_id, self.price, self.reward, self.start_location_id, self.title, self.type, self.volume)

class /corporation/{corporation_id}/mining/extractions/(Base):
    __tablename__ = /corporation/{corporation_id}/mining/extractions/

    chunk_arrival_time = Column(DateTime)
    extraction_start_time = Column(DateTime)
    moon_id = Column(Integer)
    natural_decay_time = Column(DateTime)
    structure_id = Column(Integer)

    def __repr__(self):
        return 'chunk_arrival_time={}, extraction_start_time={}, moon_id={}, natural_decay_time={}, structure_id={}'.format(self.chunk_arrival_time, self.extraction_start_time, self.moon_id, self.natural_decay_time, self.structure_id)

class /corporation/{corporation_id}/mining/observers/(Base):
    __tablename__ = /corporation/{corporation_id}/mining/observers/

    last_updated = Column(Date)
    observer_id = Column(Integer)
    observer_type = Column(String)

    def __repr__(self):
        return 'last_updated={}, observer_id={}, observer_type={}'.format(self.last_updated, self.observer_id, self.observer_type)

class /corporation/{corporation_id}/mining/observers/{observer_id}/(Base):
    __tablename__ = /corporation/{corporation_id}/mining/observers/{observer_id}/

    character_id = Column(Integer)
    last_updated = Column(Date)
    quantity = Column(Integer)
    recorded_corporation_id = Column(Integer)
    type_id = Column(Integer)

    def __repr__(self):
        return 'character_id={}, last_updated={}, quantity={}, recorded_corporation_id={}, type_id={}'.format(self.character_id, self.last_updated, self.quantity, self.recorded_corporation_id, self.type_id)

class /corporations/npccorps/(Base):
    __tablename__ = /corporations/npccorps/


    def __repr__(self):
        return ''.format()

class /corporations/{corporation_id}/(Base):
    __tablename__ = /corporations/{corporation_id}/

    alliance_id = Column(Integer)
    ceo_id = Column(Integer)
    creator_id = Column(Integer)
    date_founded = Column(DateTime)
    description = Column(String)
    faction_id = Column(Integer)
    home_station_id = Column(Integer)
    member_count = Column(Integer)
    name = Column(String)
    shares = Column(Integer)
    tax_rate = Column(Float)
    ticker = Column(String)
    url = Column(String)
    war_eligible = Column(Boolean)

    def __repr__(self):
        return 'alliance_id={}, ceo_id={}, creator_id={}, date_founded={}, description={}, faction_id={}, home_station_id={}, member_count={}, name={}, shares={}, tax_rate={}, ticker={}, url={}, war_eligible={}'.format(self.alliance_id, self.ceo_id, self.creator_id, self.date_founded, self.description, self.faction_id, self.home_station_id, self.member_count, self.name, self.shares, self.tax_rate, self.ticker, self.url, self.war_eligible)

class /corporations/{corporation_id}/alliancehistory/(Base):
    __tablename__ = /corporations/{corporation_id}/alliancehistory/

    alliance_id = Column(Integer)
    is_deleted = Column(Boolean)
    record_id = Column(Integer)
    start_date = Column(DateTime)

    def __repr__(self):
        return 'alliance_id={}, is_deleted={}, record_id={}, start_date={}'.format(self.alliance_id, self.is_deleted, self.record_id, self.start_date)

class /corporations/{corporation_id}/assets/(Base):
    __tablename__ = /corporations/{corporation_id}/assets/

    is_blueprint_copy = Column(Boolean)
    is_singleton = Column(Boolean)
    item_id = Column(Integer)
    location_flag = Column(String)
    location_id = Column(Integer)
    location_type = Column(String)
    quantity = Column(Integer)
    type_id = Column(Integer)

    def __repr__(self):
        return 'is_blueprint_copy={}, is_singleton={}, item_id={}, location_flag={}, location_id={}, location_type={}, quantity={}, type_id={}'.format(self.is_blueprint_copy, self.is_singleton, self.item_id, self.location_flag, self.location_id, self.location_type, self.quantity, self.type_id)

class /corporations/{corporation_id}/assets/locations/(Base):
    __tablename__ = /corporations/{corporation_id}/assets/locations/

    item_id = Column(Integer)
    position = Column(Object)

    def __repr__(self):
        return 'item_id={}, position={}'.format(self.item_id, self.position)

class /corporations/{corporation_id}/assets/names/(Base):
    __tablename__ = /corporations/{corporation_id}/assets/names/

    item_id = Column(Integer)
    name = Column(String)

    def __repr__(self):
        return 'item_id={}, name={}'.format(self.item_id, self.name)

class /corporations/{corporation_id}/blueprints/(Base):
    __tablename__ = /corporations/{corporation_id}/blueprints/

    item_id = Column(Integer)
    location_flag = Column(String)
    location_id = Column(Integer)
    material_efficiency = Column(Integer)
    quantity = Column(Integer)
    runs = Column(Integer)
    time_efficiency = Column(Integer)
    type_id = Column(Integer)

    def __repr__(self):
        return 'item_id={}, location_flag={}, location_id={}, material_efficiency={}, quantity={}, runs={}, time_efficiency={}, type_id={}'.format(self.item_id, self.location_flag, self.location_id, self.material_efficiency, self.quantity, self.runs, self.time_efficiency, self.type_id)

class /corporations/{corporation_id}/bookmarks/(Base):
    __tablename__ = /corporations/{corporation_id}/bookmarks/

    bookmark_id = Column(Integer)
    coordinates = Column(Object)
    created = Column(DateTime)
    creator_id = Column(Integer)
    folder_id = Column(Integer)
    item = Column(Object)
    label = Column(String)
    location_id = Column(Integer)
    notes = Column(String)

    def __repr__(self):
        return 'bookmark_id={}, coordinates={}, created={}, creator_id={}, folder_id={}, item={}, label={}, location_id={}, notes={}'.format(self.bookmark_id, self.coordinates, self.created, self.creator_id, self.folder_id, self.item, self.label, self.location_id, self.notes)

class /corporations/{corporation_id}/bookmarks/folders/(Base):
    __tablename__ = /corporations/{corporation_id}/bookmarks/folders/

    creator_id = Column(Integer)
    folder_id = Column(Integer)
    name = Column(String)

    def __repr__(self):
        return 'creator_id={}, folder_id={}, name={}'.format(self.creator_id, self.folder_id, self.name)

class /corporations/{corporation_id}/contacts/(Base):
    __tablename__ = /corporations/{corporation_id}/contacts/

    contact_id = Column(Integer)
    contact_type = Column(String)
    is_watched = Column(Boolean)
    label_ids = Column(Array)
    standing = Column(Float)

    def __repr__(self):
        return 'contact_id={}, contact_type={}, is_watched={}, label_ids={}, standing={}'.format(self.contact_id, self.contact_type, self.is_watched, self.label_ids, self.standing)

class /corporations/{corporation_id}/contacts/labels/(Base):
    __tablename__ = /corporations/{corporation_id}/contacts/labels/

    label_id = Column(Integer)
    label_name = Column(String)

    def __repr__(self):
        return 'label_id={}, label_name={}'.format(self.label_id, self.label_name)

class /corporations/{corporation_id}/containers/logs/(Base):
    __tablename__ = /corporations/{corporation_id}/containers/logs/

    action = Column(String)
    character_id = Column(Integer)
    container_id = Column(Integer)
    container_type_id = Column(Integer)
    location_flag = Column(String)
    location_id = Column(Integer)
    logged_at = Column(DateTime)
    new_config_bitmask = Column(Integer)
    old_config_bitmask = Column(Integer)
    password_type = Column(String)
    quantity = Column(Integer)
    type_id = Column(Integer)

    def __repr__(self):
        return 'action={}, character_id={}, container_id={}, container_type_id={}, location_flag={}, location_id={}, logged_at={}, new_config_bitmask={}, old_config_bitmask={}, password_type={}, quantity={}, type_id={}'.format(self.action, self.character_id, self.container_id, self.container_type_id, self.location_flag, self.location_id, self.logged_at, self.new_config_bitmask, self.old_config_bitmask, self.password_type, self.quantity, self.type_id)

class /corporations/{corporation_id}/contracts/(Base):
    __tablename__ = /corporations/{corporation_id}/contracts/

    acceptor_id = Column(Integer)
    assignee_id = Column(Integer)
    availability = Column(String)
    buyout = Column(Float)
    collateral = Column(Float)
    contract_id = Column(Integer)
    date_accepted = Column(DateTime)
    date_completed = Column(DateTime)
    date_expired = Column(DateTime)
    date_issued = Column(DateTime)
    days_to_complete = Column(Integer)
    end_location_id = Column(Integer)
    for_corporation = Column(Boolean)
    issuer_corporation_id = Column(Integer)
    issuer_id = Column(Integer)
    price = Column(Float)
    reward = Column(Float)
    start_location_id = Column(Integer)
    status = Column(String)
    title = Column(String)
    type = Column(String)
    volume = Column(Float)

    def __repr__(self):
        return 'acceptor_id={}, assignee_id={}, availability={}, buyout={}, collateral={}, contract_id={}, date_accepted={}, date_completed={}, date_expired={}, date_issued={}, days_to_complete={}, end_location_id={}, for_corporation={}, issuer_corporation_id={}, issuer_id={}, price={}, reward={}, start_location_id={}, status={}, title={}, type={}, volume={}'.format(self.acceptor_id, self.assignee_id, self.availability, self.buyout, self.collateral, self.contract_id, self.date_accepted, self.date_completed, self.date_expired, self.date_issued, self.days_to_complete, self.end_location_id, self.for_corporation, self.issuer_corporation_id, self.issuer_id, self.price, self.reward, self.start_location_id, self.status, self.title, self.type, self.volume)

class /corporations/{corporation_id}/contracts/{contract_id}/bids/(Base):
    __tablename__ = /corporations/{corporation_id}/contracts/{contract_id}/bids/

    amount = Column(Float)
    bid_id = Column(Integer)
    bidder_id = Column(Integer)
    date_bid = Column(DateTime)

    def __repr__(self):
        return 'amount={}, bid_id={}, bidder_id={}, date_bid={}'.format(self.amount, self.bid_id, self.bidder_id, self.date_bid)

class /corporations/{corporation_id}/contracts/{contract_id}/items/(Base):
    __tablename__ = /corporations/{corporation_id}/contracts/{contract_id}/items/

    is_included = Column(Boolean)
    is_singleton = Column(Boolean)
    quantity = Column(Integer)
    raw_quantity = Column(Integer)
    record_id = Column(Integer)
    type_id = Column(Integer)

    def __repr__(self):
        return 'is_included={}, is_singleton={}, quantity={}, raw_quantity={}, record_id={}, type_id={}'.format(self.is_included, self.is_singleton, self.quantity, self.raw_quantity, self.record_id, self.type_id)

class /corporations/{corporation_id}/customs_offices/(Base):
    __tablename__ = /corporations/{corporation_id}/customs_offices/

    alliance_tax_rate = Column(Float)
    allow_access_with_standings = Column(Boolean)
    allow_alliance_access = Column(Boolean)
    bad_standing_tax_rate = Column(Float)
    corporation_tax_rate = Column(Float)
    excellent_standing_tax_rate = Column(Float)
    good_standing_tax_rate = Column(Float)
    neutral_standing_tax_rate = Column(Float)
    office_id = Column(Integer)
    reinforce_exit_end = Column(Integer)
    reinforce_exit_start = Column(Integer)
    standing_level = Column(String)
    system_id = Column(Integer)
    terrible_standing_tax_rate = Column(Float)

    def __repr__(self):
        return 'alliance_tax_rate={}, allow_access_with_standings={}, allow_alliance_access={}, bad_standing_tax_rate={}, corporation_tax_rate={}, excellent_standing_tax_rate={}, good_standing_tax_rate={}, neutral_standing_tax_rate={}, office_id={}, reinforce_exit_end={}, reinforce_exit_start={}, standing_level={}, system_id={}, terrible_standing_tax_rate={}'.format(self.alliance_tax_rate, self.allow_access_with_standings, self.allow_alliance_access, self.bad_standing_tax_rate, self.corporation_tax_rate, self.excellent_standing_tax_rate, self.good_standing_tax_rate, self.neutral_standing_tax_rate, self.office_id, self.reinforce_exit_end, self.reinforce_exit_start, self.standing_level, self.system_id, self.terrible_standing_tax_rate)

class /corporations/{corporation_id}/divisions/(Base):
    __tablename__ = /corporations/{corporation_id}/divisions/

    hangar = Column(Array)
    wallet = Column(Array)

    def __repr__(self):
        return 'hangar={}, wallet={}'.format(self.hangar, self.wallet)

class /corporations/{corporation_id}/facilities/(Base):
    __tablename__ = /corporations/{corporation_id}/facilities/

    facility_id = Column(Integer)
    system_id = Column(Integer)
    type_id = Column(Integer)

    def __repr__(self):
        return 'facility_id={}, system_id={}, type_id={}'.format(self.facility_id, self.system_id, self.type_id)

class /corporations/{corporation_id}/fw/stats/(Base):
    __tablename__ = /corporations/{corporation_id}/fw/stats/

    enlisted_on = Column(DateTime)
    faction_id = Column(Integer)
    kills = Column(Object)
    pilots = Column(Integer)
    victory_points = Column(Object)

    def __repr__(self):
        return 'enlisted_on={}, faction_id={}, kills={}, pilots={}, victory_points={}'.format(self.enlisted_on, self.faction_id, self.kills, self.pilots, self.victory_points)

class /corporations/{corporation_id}/icons/(Base):
    __tablename__ = /corporations/{corporation_id}/icons/

    px128x128 = Column(String)
    px256x256 = Column(String)
    px64x64 = Column(String)

    def __repr__(self):
        return 'px128x128={}, px256x256={}, px64x64={}'.format(self.px128x128, self.px256x256, self.px64x64)

class /corporations/{corporation_id}/industry/jobs/(Base):
    __tablename__ = /corporations/{corporation_id}/industry/jobs/

    activity_id = Column(Integer)
    blueprint_id = Column(Integer)
    blueprint_location_id = Column(Integer)
    blueprint_type_id = Column(Integer)
    completed_character_id = Column(Integer)
    completed_date = Column(DateTime)
    cost = Column(Float)
    duration = Column(Integer)
    end_date = Column(DateTime)
    facility_id = Column(Integer)
    installer_id = Column(Integer)
    job_id = Column(Integer)
    licensed_runs = Column(Integer)
    location_id = Column(Integer)
    output_location_id = Column(Integer)
    pause_date = Column(DateTime)
    probability = Column(Float)
    product_type_id = Column(Integer)
    runs = Column(Integer)
    start_date = Column(DateTime)
    status = Column(String)
    successful_runs = Column(Integer)

    def __repr__(self):
        return 'activity_id={}, blueprint_id={}, blueprint_location_id={}, blueprint_type_id={}, completed_character_id={}, completed_date={}, cost={}, duration={}, end_date={}, facility_id={}, installer_id={}, job_id={}, licensed_runs={}, location_id={}, output_location_id={}, pause_date={}, probability={}, product_type_id={}, runs={}, start_date={}, status={}, successful_runs={}'.format(self.activity_id, self.blueprint_id, self.blueprint_location_id, self.blueprint_type_id, self.completed_character_id, self.completed_date, self.cost, self.duration, self.end_date, self.facility_id, self.installer_id, self.job_id, self.licensed_runs, self.location_id, self.output_location_id, self.pause_date, self.probability, self.product_type_id, self.runs, self.start_date, self.status, self.successful_runs)

class /corporations/{corporation_id}/killmails/recent/(Base):
    __tablename__ = /corporations/{corporation_id}/killmails/recent/

    killmail_hash = Column(String)
    killmail_id = Column(Integer)

    def __repr__(self):
        return 'killmail_hash={}, killmail_id={}'.format(self.killmail_hash, self.killmail_id)

class /corporations/{corporation_id}/medals/(Base):
    __tablename__ = /corporations/{corporation_id}/medals/

    created_at = Column(DateTime)
    creator_id = Column(Integer)
    description = Column(String)
    medal_id = Column(Integer)
    title = Column(String)

    def __repr__(self):
        return 'created_at={}, creator_id={}, description={}, medal_id={}, title={}'.format(self.created_at, self.creator_id, self.description, self.medal_id, self.title)

class /corporations/{corporation_id}/medals/issued/(Base):
    __tablename__ = /corporations/{corporation_id}/medals/issued/

    character_id = Column(Integer)
    issued_at = Column(DateTime)
    issuer_id = Column(Integer)
    medal_id = Column(Integer)
    reason = Column(String)
    status = Column(String)

    def __repr__(self):
        return 'character_id={}, issued_at={}, issuer_id={}, medal_id={}, reason={}, status={}'.format(self.character_id, self.issued_at, self.issuer_id, self.medal_id, self.reason, self.status)

class /corporations/{corporation_id}/members/(Base):
    __tablename__ = /corporations/{corporation_id}/members/


    def __repr__(self):
        return ''.format()

class /corporations/{corporation_id}/members/limit/(Base):
    __tablename__ = /corporations/{corporation_id}/members/limit/


    def __repr__(self):
        return ''.format()

class /corporations/{corporation_id}/members/titles/(Base):
    __tablename__ = /corporations/{corporation_id}/members/titles/

    character_id = Column(Integer)
    titles = Column(Array)

    def __repr__(self):
        return 'character_id={}, titles={}'.format(self.character_id, self.titles)

class /corporations/{corporation_id}/membertracking/(Base):
    __tablename__ = /corporations/{corporation_id}/membertracking/

    base_id = Column(Integer)
    character_id = Column(Integer)
    location_id = Column(Integer)
    logoff_date = Column(DateTime)
    logon_date = Column(DateTime)
    ship_type_id = Column(Integer)
    start_date = Column(DateTime)

    def __repr__(self):
        return 'base_id={}, character_id={}, location_id={}, logoff_date={}, logon_date={}, ship_type_id={}, start_date={}'.format(self.base_id, self.character_id, self.location_id, self.logoff_date, self.logon_date, self.ship_type_id, self.start_date)

class /corporations/{corporation_id}/orders/(Base):
    __tablename__ = /corporations/{corporation_id}/orders/

    duration = Column(Integer)
    escrow = Column(Float)
    is_buy_order = Column(Boolean)
    issued = Column(DateTime)
    issued_by = Column(Integer)
    location_id = Column(Integer)
    min_volume = Column(Integer)
    order_id = Column(Integer)
    price = Column(Float)
    range = Column(String)
    region_id = Column(Integer)
    type_id = Column(Integer)
    volume_remain = Column(Integer)
    volume_total = Column(Integer)
    wallet_division = Column(Integer)

    def __repr__(self):
        return 'duration={}, escrow={}, is_buy_order={}, issued={}, issued_by={}, location_id={}, min_volume={}, order_id={}, price={}, range={}, region_id={}, type_id={}, volume_remain={}, volume_total={}, wallet_division={}'.format(self.duration, self.escrow, self.is_buy_order, self.issued, self.issued_by, self.location_id, self.min_volume, self.order_id, self.price, self.range, self.region_id, self.type_id, self.volume_remain, self.volume_total, self.wallet_division)

class /corporations/{corporation_id}/orders/history/(Base):
    __tablename__ = /corporations/{corporation_id}/orders/history/

    duration = Column(Integer)
    escrow = Column(Float)
    is_buy_order = Column(Boolean)
    issued = Column(DateTime)
    issued_by = Column(Integer)
    location_id = Column(Integer)
    min_volume = Column(Integer)
    order_id = Column(Integer)
    price = Column(Float)
    range = Column(String)
    region_id = Column(Integer)
    state = Column(String)
    type_id = Column(Integer)
    volume_remain = Column(Integer)
    volume_total = Column(Integer)
    wallet_division = Column(Integer)

    def __repr__(self):
        return 'duration={}, escrow={}, is_buy_order={}, issued={}, issued_by={}, location_id={}, min_volume={}, order_id={}, price={}, range={}, region_id={}, state={}, type_id={}, volume_remain={}, volume_total={}, wallet_division={}'.format(self.duration, self.escrow, self.is_buy_order, self.issued, self.issued_by, self.location_id, self.min_volume, self.order_id, self.price, self.range, self.region_id, self.state, self.type_id, self.volume_remain, self.volume_total, self.wallet_division)

class /corporations/{corporation_id}/roles/(Base):
    __tablename__ = /corporations/{corporation_id}/roles/

    character_id = Column(Integer)
    grantable_roles = Column(Array)
    grantable_roles_at_base = Column(Array)
    grantable_roles_at_hq = Column(Array)
    grantable_roles_at_other = Column(Array)
    roles = Column(Array)
    roles_at_base = Column(Array)
    roles_at_hq = Column(Array)
    roles_at_other = Column(Array)

    def __repr__(self):
        return 'character_id={}, grantable_roles={}, grantable_roles_at_base={}, grantable_roles_at_hq={}, grantable_roles_at_other={}, roles={}, roles_at_base={}, roles_at_hq={}, roles_at_other={}'.format(self.character_id, self.grantable_roles, self.grantable_roles_at_base, self.grantable_roles_at_hq, self.grantable_roles_at_other, self.roles, self.roles_at_base, self.roles_at_hq, self.roles_at_other)

class /corporations/{corporation_id}/roles/history/(Base):
    __tablename__ = /corporations/{corporation_id}/roles/history/

    changed_at = Column(DateTime)
    character_id = Column(Integer)
    issuer_id = Column(Integer)
    new_roles = Column(Array)
    old_roles = Column(Array)
    role_type = Column(String)

    def __repr__(self):
        return 'changed_at={}, character_id={}, issuer_id={}, new_roles={}, old_roles={}, role_type={}'.format(self.changed_at, self.character_id, self.issuer_id, self.new_roles, self.old_roles, self.role_type)

class /corporations/{corporation_id}/shareholders/(Base):
    __tablename__ = /corporations/{corporation_id}/shareholders/

    share_count = Column(Integer)
    shareholder_id = Column(Integer)
    shareholder_type = Column(String)

    def __repr__(self):
        return 'share_count={}, shareholder_id={}, shareholder_type={}'.format(self.share_count, self.shareholder_id, self.shareholder_type)

class /corporations/{corporation_id}/standings/(Base):
    __tablename__ = /corporations/{corporation_id}/standings/

    from_id = Column(Integer)
    from_type = Column(String)
    standing = Column(Float)

    def __repr__(self):
        return 'from_id={}, from_type={}, standing={}'.format(self.from_id, self.from_type, self.standing)

class /corporations/{corporation_id}/starbases/(Base):
    __tablename__ = /corporations/{corporation_id}/starbases/

    moon_id = Column(Integer)
    onlined_since = Column(DateTime)
    reinforced_until = Column(DateTime)
    starbase_id = Column(Integer)
    state = Column(String)
    system_id = Column(Integer)
    type_id = Column(Integer)
    unanchor_at = Column(DateTime)

    def __repr__(self):
        return 'moon_id={}, onlined_since={}, reinforced_until={}, starbase_id={}, state={}, system_id={}, type_id={}, unanchor_at={}'.format(self.moon_id, self.onlined_since, self.reinforced_until, self.starbase_id, self.state, self.system_id, self.type_id, self.unanchor_at)

class /corporations/{corporation_id}/starbases/{starbase_id}/(Base):
    __tablename__ = /corporations/{corporation_id}/starbases/{starbase_id}/

    allow_alliance_members = Column(Boolean)
    allow_corporation_members = Column(Boolean)
    anchor = Column(String)
    attack_if_at_war = Column(Boolean)
    attack_if_other_security_status_dropping = Column(Boolean)
    attack_security_status_threshold = Column(Float)
    attack_standing_threshold = Column(Float)
    fuel_bay_take = Column(String)
    fuel_bay_view = Column(String)
    fuels = Column(Array)
    offline = Column(String)
    online = Column(String)
    unanchor = Column(String)
    use_alliance_standings = Column(Boolean)

    def __repr__(self):
        return 'allow_alliance_members={}, allow_corporation_members={}, anchor={}, attack_if_at_war={}, attack_if_other_security_status_dropping={}, attack_security_status_threshold={}, attack_standing_threshold={}, fuel_bay_take={}, fuel_bay_view={}, fuels={}, offline={}, online={}, unanchor={}, use_alliance_standings={}'.format(self.allow_alliance_members, self.allow_corporation_members, self.anchor, self.attack_if_at_war, self.attack_if_other_security_status_dropping, self.attack_security_status_threshold, self.attack_standing_threshold, self.fuel_bay_take, self.fuel_bay_view, self.fuels, self.offline, self.online, self.unanchor, self.use_alliance_standings)

class /corporations/{corporation_id}/structures/(Base):
    __tablename__ = /corporations/{corporation_id}/structures/

    corporation_id = Column(Integer)
    fuel_expires = Column(DateTime)
    name = Column(String)
    next_reinforce_apply = Column(DateTime)
    next_reinforce_hour = Column(Integer)
    profile_id = Column(Integer)
    reinforce_hour = Column(Integer)
    services = Column(Array)
    state = Column(String)
    state_timer_end = Column(DateTime)
    state_timer_start = Column(DateTime)
    structure_id = Column(Integer)
    system_id = Column(Integer)
    type_id = Column(Integer)
    unanchors_at = Column(DateTime)

    def __repr__(self):
        return 'corporation_id={}, fuel_expires={}, name={}, next_reinforce_apply={}, next_reinforce_hour={}, profile_id={}, reinforce_hour={}, services={}, state={}, state_timer_end={}, state_timer_start={}, structure_id={}, system_id={}, type_id={}, unanchors_at={}'.format(self.corporation_id, self.fuel_expires, self.name, self.next_reinforce_apply, self.next_reinforce_hour, self.profile_id, self.reinforce_hour, self.services, self.state, self.state_timer_end, self.state_timer_start, self.structure_id, self.system_id, self.type_id, self.unanchors_at)

class /corporations/{corporation_id}/titles/(Base):
    __tablename__ = /corporations/{corporation_id}/titles/

    grantable_roles = Column(Array)
    grantable_roles_at_base = Column(Array)
    grantable_roles_at_hq = Column(Array)
    grantable_roles_at_other = Column(Array)
    name = Column(String)
    roles = Column(Array)
    roles_at_base = Column(Array)
    roles_at_hq = Column(Array)
    roles_at_other = Column(Array)
    title_id = Column(Integer)

    def __repr__(self):
        return 'grantable_roles={}, grantable_roles_at_base={}, grantable_roles_at_hq={}, grantable_roles_at_other={}, name={}, roles={}, roles_at_base={}, roles_at_hq={}, roles_at_other={}, title_id={}'.format(self.grantable_roles, self.grantable_roles_at_base, self.grantable_roles_at_hq, self.grantable_roles_at_other, self.name, self.roles, self.roles_at_base, self.roles_at_hq, self.roles_at_other, self.title_id)

class /corporations/{corporation_id}/wallets/(Base):
    __tablename__ = /corporations/{corporation_id}/wallets/

    balance = Column(Float)
    division = Column(Integer)

    def __repr__(self):
        return 'balance={}, division={}'.format(self.balance, self.division)

class /corporations/{corporation_id}/wallets/{division}/journal/(Base):
    __tablename__ = /corporations/{corporation_id}/wallets/{division}/journal/

    amount = Column(Float)
    balance = Column(Float)
    context_id = Column(Integer)
    context_id_type = Column(String)
    date = Column(DateTime)
    description = Column(String)
    first_party_id = Column(Integer)
    id = Column(Integer)
    reason = Column(String)
    ref_type = Column(String)
    second_party_id = Column(Integer)
    tax = Column(Float)
    tax_receiver_id = Column(Integer)

    def __repr__(self):
        return 'amount={}, balance={}, context_id={}, context_id_type={}, date={}, description={}, first_party_id={}, id={}, reason={}, ref_type={}, second_party_id={}, tax={}, tax_receiver_id={}'.format(self.amount, self.balance, self.context_id, self.context_id_type, self.date, self.description, self.first_party_id, self.id, self.reason, self.ref_type, self.second_party_id, self.tax, self.tax_receiver_id)

class /corporations/{corporation_id}/wallets/{division}/transactions/(Base):
    __tablename__ = /corporations/{corporation_id}/wallets/{division}/transactions/

    client_id = Column(Integer)
    date = Column(DateTime)
    is_buy = Column(Boolean)
    journal_ref_id = Column(Integer)
    location_id = Column(Integer)
    quantity = Column(Integer)
    transaction_id = Column(Integer)
    type_id = Column(Integer)
    unit_price = Column(Float)

    def __repr__(self):
        return 'client_id={}, date={}, is_buy={}, journal_ref_id={}, location_id={}, quantity={}, transaction_id={}, type_id={}, unit_price={}'.format(self.client_id, self.date, self.is_buy, self.journal_ref_id, self.location_id, self.quantity, self.transaction_id, self.type_id, self.unit_price)

class /dogma/attributes/(Base):
    __tablename__ = /dogma/attributes/


    def __repr__(self):
        return ''.format()

class /dogma/attributes/{attribute_id}/(Base):
    __tablename__ = /dogma/attributes/{attribute_id}/

    attribute_id = Column(Integer)
    default_value = Column(Float)
    description = Column(String)
    display_name = Column(String)
    high_is_good = Column(Boolean)
    icon_id = Column(Integer)
    name = Column(String)
    published = Column(Boolean)
    stackable = Column(Boolean)
    unit_id = Column(Integer)

    def __repr__(self):
        return 'attribute_id={}, default_value={}, description={}, display_name={}, high_is_good={}, icon_id={}, name={}, published={}, stackable={}, unit_id={}'.format(self.attribute_id, self.default_value, self.description, self.display_name, self.high_is_good, self.icon_id, self.name, self.published, self.stackable, self.unit_id)

class /dogma/dynamic/items/{type_id}/{item_id}/(Base):
    __tablename__ = /dogma/dynamic/items/{type_id}/{item_id}/

    created_by = Column(Integer)
    dogma_attributes = Column(Array)
    dogma_effects = Column(Array)
    mutator_type_id = Column(Integer)
    source_type_id = Column(Integer)

    def __repr__(self):
        return 'created_by={}, dogma_attributes={}, dogma_effects={}, mutator_type_id={}, source_type_id={}'.format(self.created_by, self.dogma_attributes, self.dogma_effects, self.mutator_type_id, self.source_type_id)

class /dogma/effects/(Base):
    __tablename__ = /dogma/effects/


    def __repr__(self):
        return ''.format()

class /dogma/effects/{effect_id}/(Base):
    __tablename__ = /dogma/effects/{effect_id}/

    description = Column(String)
    disallow_auto_repeat = Column(Boolean)
    discharge_attribute_id = Column(Integer)
    display_name = Column(String)
    duration_attribute_id = Column(Integer)
    effect_category = Column(Integer)
    effect_id = Column(Integer)
    electronic_chance = Column(Boolean)
    falloff_attribute_id = Column(Integer)
    icon_id = Column(Integer)
    is_assistance = Column(Boolean)
    is_offensive = Column(Boolean)
    is_warp_safe = Column(Boolean)
    modifiers = Column(Array)
    name = Column(String)
    post_expression = Column(Integer)
    pre_expression = Column(Integer)
    published = Column(Boolean)
    range_attribute_id = Column(Integer)
    range_chance = Column(Boolean)
    tracking_speed_attribute_id = Column(Integer)

    def __repr__(self):
        return 'description={}, disallow_auto_repeat={}, discharge_attribute_id={}, display_name={}, duration_attribute_id={}, effect_category={}, effect_id={}, electronic_chance={}, falloff_attribute_id={}, icon_id={}, is_assistance={}, is_offensive={}, is_warp_safe={}, modifiers={}, name={}, post_expression={}, pre_expression={}, published={}, range_attribute_id={}, range_chance={}, tracking_speed_attribute_id={}'.format(self.description, self.disallow_auto_repeat, self.discharge_attribute_id, self.display_name, self.duration_attribute_id, self.effect_category, self.effect_id, self.electronic_chance, self.falloff_attribute_id, self.icon_id, self.is_assistance, self.is_offensive, self.is_warp_safe, self.modifiers, self.name, self.post_expression, self.pre_expression, self.published, self.range_attribute_id, self.range_chance, self.tracking_speed_attribute_id)

class /fleets/{fleet_id}/(Base):
    __tablename__ = /fleets/{fleet_id}/

    is_free_move = Column(Boolean)
    is_registered = Column(Boolean)
    is_voice_enabled = Column(Boolean)
    motd = Column(String)

    def __repr__(self):
        return 'is_free_move={}, is_registered={}, is_voice_enabled={}, motd={}'.format(self.is_free_move, self.is_registered, self.is_voice_enabled, self.motd)

class /fleets/{fleet_id}/members/(Base):
    __tablename__ = /fleets/{fleet_id}/members/

    character_id = Column(Integer)
    join_time = Column(DateTime)
    role = Column(String)
    role_name = Column(String)
    ship_type_id = Column(Integer)
    solar_system_id = Column(Integer)
    squad_id = Column(Integer)
    station_id = Column(Integer)
    takes_fleet_warp = Column(Boolean)
    wing_id = Column(Integer)

    def __repr__(self):
        return 'character_id={}, join_time={}, role={}, role_name={}, ship_type_id={}, solar_system_id={}, squad_id={}, station_id={}, takes_fleet_warp={}, wing_id={}'.format(self.character_id, self.join_time, self.role, self.role_name, self.ship_type_id, self.solar_system_id, self.squad_id, self.station_id, self.takes_fleet_warp, self.wing_id)

class /fleets/{fleet_id}/members/{member_id}/(Base):
    __tablename__ = /fleets/{fleet_id}/members/{member_id}/

    character_id = Column(Integer)
    join_time = Column(DateTime)
    role = Column(String)
    role_name = Column(String)
    ship_type_id = Column(Integer)
    solar_system_id = Column(Integer)
    squad_id = Column(Integer)
    station_id = Column(Integer)
    takes_fleet_warp = Column(Boolean)
    wing_id = Column(Integer)

    def __repr__(self):
        return 'character_id={}, join_time={}, role={}, role_name={}, ship_type_id={}, solar_system_id={}, squad_id={}, station_id={}, takes_fleet_warp={}, wing_id={}'.format(self.character_id, self.join_time, self.role, self.role_name, self.ship_type_id, self.solar_system_id, self.squad_id, self.station_id, self.takes_fleet_warp, self.wing_id)

class /fleets/{fleet_id}/squads/{squad_id}/(Base):
    __tablename__ = /fleets/{fleet_id}/squads/{squad_id}/

    character_id = Column(Integer)
    join_time = Column(DateTime)
    role = Column(String)
    role_name = Column(String)
    ship_type_id = Column(Integer)
    solar_system_id = Column(Integer)
    squad_id = Column(Integer)
    station_id = Column(Integer)
    takes_fleet_warp = Column(Boolean)
    wing_id = Column(Integer)

    def __repr__(self):
        return 'character_id={}, join_time={}, role={}, role_name={}, ship_type_id={}, solar_system_id={}, squad_id={}, station_id={}, takes_fleet_warp={}, wing_id={}'.format(self.character_id, self.join_time, self.role, self.role_name, self.ship_type_id, self.solar_system_id, self.squad_id, self.station_id, self.takes_fleet_warp, self.wing_id)

class /fleets/{fleet_id}/wings/(Base):
    __tablename__ = /fleets/{fleet_id}/wings/

    id = Column(Integer)
    name = Column(String)
    squads = Column(Array)

    def __repr__(self):
        return 'id={}, name={}, squads={}'.format(self.id, self.name, self.squads)

class /fleets/{fleet_id}/wings/{wing_id}/(Base):
    __tablename__ = /fleets/{fleet_id}/wings/{wing_id}/

    id = Column(Integer)
    name = Column(String)
    squads = Column(Array)

    def __repr__(self):
        return 'id={}, name={}, squads={}'.format(self.id, self.name, self.squads)

class /fw/leaderboards/(Base):
    __tablename__ = /fw/leaderboards/

    kills = Column(Object)
    victory_points = Column(Object)

    def __repr__(self):
        return 'kills={}, victory_points={}'.format(self.kills, self.victory_points)

class /fw/leaderboards/characters/(Base):
    __tablename__ = /fw/leaderboards/characters/

    kills = Column(Object)
    victory_points = Column(Object)

    def __repr__(self):
        return 'kills={}, victory_points={}'.format(self.kills, self.victory_points)

class /fw/leaderboards/corporations/(Base):
    __tablename__ = /fw/leaderboards/corporations/

    kills = Column(Object)
    victory_points = Column(Object)

    def __repr__(self):
        return 'kills={}, victory_points={}'.format(self.kills, self.victory_points)

class /fw/stats/(Base):
    __tablename__ = /fw/stats/

    faction_id = Column(Integer)
    kills = Column(Object)
    pilots = Column(Integer)
    systems_controlled = Column(Integer)
    victory_points = Column(Object)

    def __repr__(self):
        return 'faction_id={}, kills={}, pilots={}, systems_controlled={}, victory_points={}'.format(self.faction_id, self.kills, self.pilots, self.systems_controlled, self.victory_points)

class /fw/systems/(Base):
    __tablename__ = /fw/systems/

    contested = Column(String)
    occupier_faction_id = Column(Integer)
    owner_faction_id = Column(Integer)
    solar_system_id = Column(Integer)
    victory_points = Column(Integer)
    victory_points_threshold = Column(Integer)

    def __repr__(self):
        return 'contested={}, occupier_faction_id={}, owner_faction_id={}, solar_system_id={}, victory_points={}, victory_points_threshold={}'.format(self.contested, self.occupier_faction_id, self.owner_faction_id, self.solar_system_id, self.victory_points, self.victory_points_threshold)

class /fw/wars/(Base):
    __tablename__ = /fw/wars/

    against_id = Column(Integer)
    faction_id = Column(Integer)

    def __repr__(self):
        return 'against_id={}, faction_id={}'.format(self.against_id, self.faction_id)

class /incursions/(Base):
    __tablename__ = /incursions/

    constellation_id = Column(Integer)
    faction_id = Column(Integer)
    has_boss = Column(Boolean)
    infested_solar_systems = Column(Array)
    influence = Column(Float)
    staging_solar_system_id = Column(Integer)
    state = Column(String)
    type = Column(String)

    def __repr__(self):
        return 'constellation_id={}, faction_id={}, has_boss={}, infested_solar_systems={}, influence={}, staging_solar_system_id={}, state={}, type={}'.format(self.constellation_id, self.faction_id, self.has_boss, self.infested_solar_systems, self.influence, self.staging_solar_system_id, self.state, self.type)

class /industry/facilities/(Base):
    __tablename__ = /industry/facilities/

    facility_id = Column(Integer)
    owner_id = Column(Integer)
    region_id = Column(Integer)
    solar_system_id = Column(Integer)
    tax = Column(Float)
    type_id = Column(Integer)

    def __repr__(self):
        return 'facility_id={}, owner_id={}, region_id={}, solar_system_id={}, tax={}, type_id={}'.format(self.facility_id, self.owner_id, self.region_id, self.solar_system_id, self.tax, self.type_id)

class /industry/systems/(Base):
    __tablename__ = /industry/systems/

    cost_indices = Column(Array)
    solar_system_id = Column(Integer)

    def __repr__(self):
        return 'cost_indices={}, solar_system_id={}'.format(self.cost_indices, self.solar_system_id)

class /insurance/prices/(Base):
    __tablename__ = /insurance/prices/

    levels = Column(Array)
    type_id = Column(Integer)

    def __repr__(self):
        return 'levels={}, type_id={}'.format(self.levels, self.type_id)

class /killmails/{killmail_id}/{killmail_hash}/(Base):
    __tablename__ = /killmails/{killmail_id}/{killmail_hash}/

    attackers = Column(Array)
    killmail_id = Column(Integer)
    killmail_time = Column(DateTime)
    moon_id = Column(Integer)
    solar_system_id = Column(Integer)
    victim = Column(Object)
    war_id = Column(Integer)

    def __repr__(self):
        return 'attackers={}, killmail_id={}, killmail_time={}, moon_id={}, solar_system_id={}, victim={}, war_id={}'.format(self.attackers, self.killmail_id, self.killmail_time, self.moon_id, self.solar_system_id, self.victim, self.war_id)

class /loyalty/stores/{corporation_id}/offers/(Base):
    __tablename__ = /loyalty/stores/{corporation_id}/offers/

    ak_cost = Column(Integer)
    isk_cost = Column(Integer)
    lp_cost = Column(Integer)
    offer_id = Column(Integer)
    quantity = Column(Integer)
    required_items = Column(Array)
    type_id = Column(Integer)

    def __repr__(self):
        return 'ak_cost={}, isk_cost={}, lp_cost={}, offer_id={}, quantity={}, required_items={}, type_id={}'.format(self.ak_cost, self.isk_cost, self.lp_cost, self.offer_id, self.quantity, self.required_items, self.type_id)

class /markets/groups/(Base):
    __tablename__ = /markets/groups/


    def __repr__(self):
        return ''.format()

class /markets/groups/{market_group_id}/(Base):
    __tablename__ = /markets/groups/{market_group_id}/

    description = Column(String)
    market_group_id = Column(Integer)
    name = Column(String)
    parent_group_id = Column(Integer)
    types = Column(Array)

    def __repr__(self):
        return 'description={}, market_group_id={}, name={}, parent_group_id={}, types={}'.format(self.description, self.market_group_id, self.name, self.parent_group_id, self.types)

class /markets/prices/(Base):
    __tablename__ = /markets/prices/

    adjusted_price = Column(Float)
    average_price = Column(Float)
    type_id = Column(Integer)

    def __repr__(self):
        return 'adjusted_price={}, average_price={}, type_id={}'.format(self.adjusted_price, self.average_price, self.type_id)

class /markets/structures/{structure_id}/(Base):
    __tablename__ = /markets/structures/{structure_id}/

    duration = Column(Integer)
    is_buy_order = Column(Boolean)
    issued = Column(DateTime)
    location_id = Column(Integer)
    min_volume = Column(Integer)
    order_id = Column(Integer)
    price = Column(Float)
    range = Column(String)
    type_id = Column(Integer)
    volume_remain = Column(Integer)
    volume_total = Column(Integer)

    def __repr__(self):
        return 'duration={}, is_buy_order={}, issued={}, location_id={}, min_volume={}, order_id={}, price={}, range={}, type_id={}, volume_remain={}, volume_total={}'.format(self.duration, self.is_buy_order, self.issued, self.location_id, self.min_volume, self.order_id, self.price, self.range, self.type_id, self.volume_remain, self.volume_total)

class /markets/{region_id}/history/(Base):
    __tablename__ = /markets/{region_id}/history/

    average = Column(Float)
    date = Column(Date)
    highest = Column(Float)
    lowest = Column(Float)
    order_count = Column(Integer)
    volume = Column(Integer)

    def __repr__(self):
        return 'average={}, date={}, highest={}, lowest={}, order_count={}, volume={}'.format(self.average, self.date, self.highest, self.lowest, self.order_count, self.volume)

class /markets/{region_id}/orders/(Base):
    __tablename__ = /markets/{region_id}/orders/

    duration = Column(Integer)
    is_buy_order = Column(Boolean)
    issued = Column(DateTime)
    location_id = Column(Integer)
    min_volume = Column(Integer)
    order_id = Column(Integer)
    price = Column(Float)
    range = Column(String)
    system_id = Column(Integer)
    type_id = Column(Integer)
    volume_remain = Column(Integer)
    volume_total = Column(Integer)

    def __repr__(self):
        return 'duration={}, is_buy_order={}, issued={}, location_id={}, min_volume={}, order_id={}, price={}, range={}, system_id={}, type_id={}, volume_remain={}, volume_total={}'.format(self.duration, self.is_buy_order, self.issued, self.location_id, self.min_volume, self.order_id, self.price, self.range, self.system_id, self.type_id, self.volume_remain, self.volume_total)

class /markets/{region_id}/types/(Base):
    __tablename__ = /markets/{region_id}/types/


    def __repr__(self):
        return ''.format()

class /opportunities/groups/(Base):
    __tablename__ = /opportunities/groups/


    def __repr__(self):
        return ''.format()

class /opportunities/groups/{group_id}/(Base):
    __tablename__ = /opportunities/groups/{group_id}/

    connected_groups = Column(Array)
    description = Column(String)
    group_id = Column(Integer)
    name = Column(String)
    notification = Column(String)
    required_tasks = Column(Array)

    def __repr__(self):
        return 'connected_groups={}, description={}, group_id={}, name={}, notification={}, required_tasks={}'.format(self.connected_groups, self.description, self.group_id, self.name, self.notification, self.required_tasks)

class /opportunities/tasks/(Base):
    __tablename__ = /opportunities/tasks/


    def __repr__(self):
        return ''.format()

class /opportunities/tasks/{task_id}/(Base):
    __tablename__ = /opportunities/tasks/{task_id}/

    description = Column(String)
    name = Column(String)
    notification = Column(String)
    task_id = Column(Integer)

    def __repr__(self):
        return 'description={}, name={}, notification={}, task_id={}'.format(self.description, self.name, self.notification, self.task_id)

class /route/{origin}/{destination}/(Base):
    __tablename__ = /route/{origin}/{destination}/


    def __repr__(self):
        return ''.format()

class /search/(Base):
    __tablename__ = /search/

    agent = Column(Array)
    alliance = Column(Array)
    character = Column(Array)
    constellation = Column(Array)
    corporation = Column(Array)
    faction = Column(Array)
    inventory_type = Column(Array)
    region = Column(Array)
    solar_system = Column(Array)
    station = Column(Array)

    def __repr__(self):
        return 'agent={}, alliance={}, character={}, constellation={}, corporation={}, faction={}, inventory_type={}, region={}, solar_system={}, station={}'.format(self.agent, self.alliance, self.character, self.constellation, self.corporation, self.faction, self.inventory_type, self.region, self.solar_system, self.station)

class /sovereignty/campaigns/(Base):
    __tablename__ = /sovereignty/campaigns/

    attackers_score = Column(Float)
    campaign_id = Column(Integer)
    constellation_id = Column(Integer)
    defender_id = Column(Integer)
    defender_score = Column(Float)
    event_type = Column(String)
    participants = Column(Array)
    solar_system_id = Column(Integer)
    start_time = Column(DateTime)
    structure_id = Column(Integer)

    def __repr__(self):
        return 'attackers_score={}, campaign_id={}, constellation_id={}, defender_id={}, defender_score={}, event_type={}, participants={}, solar_system_id={}, start_time={}, structure_id={}'.format(self.attackers_score, self.campaign_id, self.constellation_id, self.defender_id, self.defender_score, self.event_type, self.participants, self.solar_system_id, self.start_time, self.structure_id)

class /sovereignty/map/(Base):
    __tablename__ = /sovereignty/map/

    alliance_id = Column(Integer)
    corporation_id = Column(Integer)
    faction_id = Column(Integer)
    system_id = Column(Integer)

    def __repr__(self):
        return 'alliance_id={}, corporation_id={}, faction_id={}, system_id={}'.format(self.alliance_id, self.corporation_id, self.faction_id, self.system_id)

class /sovereignty/structures/(Base):
    __tablename__ = /sovereignty/structures/

    alliance_id = Column(Integer)
    solar_system_id = Column(Integer)
    structure_id = Column(Integer)
    structure_type_id = Column(Integer)
    vulnerability_occupancy_level = Column(Float)
    vulnerable_end_time = Column(DateTime)
    vulnerable_start_time = Column(DateTime)

    def __repr__(self):
        return 'alliance_id={}, solar_system_id={}, structure_id={}, structure_type_id={}, vulnerability_occupancy_level={}, vulnerable_end_time={}, vulnerable_start_time={}'.format(self.alliance_id, self.solar_system_id, self.structure_id, self.structure_type_id, self.vulnerability_occupancy_level, self.vulnerable_end_time, self.vulnerable_start_time)

class /status/(Base):
    __tablename__ = /status/

    players = Column(Integer)
    server_version = Column(String)
    start_time = Column(DateTime)
    vip = Column(Boolean)

    def __repr__(self):
        return 'players={}, server_version={}, start_time={}, vip={}'.format(self.players, self.server_version, self.start_time, self.vip)

class /universe/ancestries/(Base):
    __tablename__ = /universe/ancestries/

    bloodline_id = Column(Integer)
    description = Column(String)
    icon_id = Column(Integer)
    id = Column(Integer)
    name = Column(String)
    short_description = Column(String)

    def __repr__(self):
        return 'bloodline_id={}, description={}, icon_id={}, id={}, name={}, short_description={}'.format(self.bloodline_id, self.description, self.icon_id, self.id, self.name, self.short_description)

class /universe/asteroid_belts/{asteroid_belt_id}/(Base):
    __tablename__ = /universe/asteroid_belts/{asteroid_belt_id}/

    name = Column(String)
    position = Column(Object)
    system_id = Column(Integer)

    def __repr__(self):
        return 'name={}, position={}, system_id={}'.format(self.name, self.position, self.system_id)

class /universe/bloodlines/(Base):
    __tablename__ = /universe/bloodlines/

    bloodline_id = Column(Integer)
    charisma = Column(Integer)
    corporation_id = Column(Integer)
    description = Column(String)
    intelligence = Column(Integer)
    memory = Column(Integer)
    name = Column(String)
    perception = Column(Integer)
    race_id = Column(Integer)
    ship_type_id = Column(Integer)
    willpower = Column(Integer)

    def __repr__(self):
        return 'bloodline_id={}, charisma={}, corporation_id={}, description={}, intelligence={}, memory={}, name={}, perception={}, race_id={}, ship_type_id={}, willpower={}'.format(self.bloodline_id, self.charisma, self.corporation_id, self.description, self.intelligence, self.memory, self.name, self.perception, self.race_id, self.ship_type_id, self.willpower)

class /universe/categories/(Base):
    __tablename__ = /universe/categories/


    def __repr__(self):
        return ''.format()

class /universe/categories/{category_id}/(Base):
    __tablename__ = /universe/categories/{category_id}/

    category_id = Column(Integer)
    groups = Column(Array)
    name = Column(String)
    published = Column(Boolean)

    def __repr__(self):
        return 'category_id={}, groups={}, name={}, published={}'.format(self.category_id, self.groups, self.name, self.published)

class /universe/constellations/(Base):
    __tablename__ = /universe/constellations/


    def __repr__(self):
        return ''.format()

class /universe/constellations/{constellation_id}/(Base):
    __tablename__ = /universe/constellations/{constellation_id}/

    constellation_id = Column(Integer)
    name = Column(String)
    position = Column(Object)
    region_id = Column(Integer)
    systems = Column(Array)

    def __repr__(self):
        return 'constellation_id={}, name={}, position={}, region_id={}, systems={}'.format(self.constellation_id, self.name, self.position, self.region_id, self.systems)

class /universe/factions/(Base):
    __tablename__ = /universe/factions/

    corporation_id = Column(Integer)
    description = Column(String)
    faction_id = Column(Integer)
    is_unique = Column(Boolean)
    militia_corporation_id = Column(Integer)
    name = Column(String)
    size_factor = Column(Float)
    solar_system_id = Column(Integer)
    station_count = Column(Integer)
    station_system_count = Column(Integer)

    def __repr__(self):
        return 'corporation_id={}, description={}, faction_id={}, is_unique={}, militia_corporation_id={}, name={}, size_factor={}, solar_system_id={}, station_count={}, station_system_count={}'.format(self.corporation_id, self.description, self.faction_id, self.is_unique, self.militia_corporation_id, self.name, self.size_factor, self.solar_system_id, self.station_count, self.station_system_count)

class /universe/graphics/(Base):
    __tablename__ = /universe/graphics/


    def __repr__(self):
        return ''.format()

class /universe/graphics/{graphic_id}/(Base):
    __tablename__ = /universe/graphics/{graphic_id}/

    collision_file = Column(String)
    graphic_file = Column(String)
    graphic_id = Column(Integer)
    icon_folder = Column(String)
    sof_dna = Column(String)
    sof_fation_name = Column(String)
    sof_hull_name = Column(String)
    sof_race_name = Column(String)

    def __repr__(self):
        return 'collision_file={}, graphic_file={}, graphic_id={}, icon_folder={}, sof_dna={}, sof_fation_name={}, sof_hull_name={}, sof_race_name={}'.format(self.collision_file, self.graphic_file, self.graphic_id, self.icon_folder, self.sof_dna, self.sof_fation_name, self.sof_hull_name, self.sof_race_name)

class /universe/groups/(Base):
    __tablename__ = /universe/groups/


    def __repr__(self):
        return ''.format()

class /universe/groups/{group_id}/(Base):
    __tablename__ = /universe/groups/{group_id}/

    category_id = Column(Integer)
    group_id = Column(Integer)
    name = Column(String)
    published = Column(Boolean)
    types = Column(Array)

    def __repr__(self):
        return 'category_id={}, group_id={}, name={}, published={}, types={}'.format(self.category_id, self.group_id, self.name, self.published, self.types)

class /universe/ids/(Base):
    __tablename__ = /universe/ids/

    agents = Column(Array)
    alliances = Column(Array)
    characters = Column(Array)
    constellations = Column(Array)
    corporations = Column(Array)
    factions = Column(Array)
    inventory_types = Column(Array)
    regions = Column(Array)
    stations = Column(Array)
    systems = Column(Array)

    def __repr__(self):
        return 'agents={}, alliances={}, characters={}, constellations={}, corporations={}, factions={}, inventory_types={}, regions={}, stations={}, systems={}'.format(self.agents, self.alliances, self.characters, self.constellations, self.corporations, self.factions, self.inventory_types, self.regions, self.stations, self.systems)

class /universe/moons/{moon_id}/(Base):
    __tablename__ = /universe/moons/{moon_id}/

    moon_id = Column(Integer)
    name = Column(String)
    position = Column(Object)
    system_id = Column(Integer)

    def __repr__(self):
        return 'moon_id={}, name={}, position={}, system_id={}'.format(self.moon_id, self.name, self.position, self.system_id)

class /universe/names/(Base):
    __tablename__ = /universe/names/

    category = Column(String)
    id = Column(Integer)
    name = Column(String)

    def __repr__(self):
        return 'category={}, id={}, name={}'.format(self.category, self.id, self.name)

class /universe/planets/{planet_id}/(Base):
    __tablename__ = /universe/planets/{planet_id}/

    name = Column(String)
    planet_id = Column(Integer)
    position = Column(Object)
    system_id = Column(Integer)
    type_id = Column(Integer)

    def __repr__(self):
        return 'name={}, planet_id={}, position={}, system_id={}, type_id={}'.format(self.name, self.planet_id, self.position, self.system_id, self.type_id)

class /universe/races/(Base):
    __tablename__ = /universe/races/

    alliance_id = Column(Integer)
    description = Column(String)
    name = Column(String)
    race_id = Column(Integer)

    def __repr__(self):
        return 'alliance_id={}, description={}, name={}, race_id={}'.format(self.alliance_id, self.description, self.name, self.race_id)

class /universe/regions/(Base):
    __tablename__ = /universe/regions/


    def __repr__(self):
        return ''.format()

class /universe/regions/{region_id}/(Base):
    __tablename__ = /universe/regions/{region_id}/

    constellations = Column(Array)
    description = Column(String)
    name = Column(String)
    region_id = Column(Integer)

    def __repr__(self):
        return 'constellations={}, description={}, name={}, region_id={}'.format(self.constellations, self.description, self.name, self.region_id)

class /universe/schematics/{schematic_id}/(Base):
    __tablename__ = /universe/schematics/{schematic_id}/

    cycle_time = Column(Integer)
    schematic_name = Column(String)

    def __repr__(self):
        return 'cycle_time={}, schematic_name={}'.format(self.cycle_time, self.schematic_name)

class /universe/stargates/{stargate_id}/(Base):
    __tablename__ = /universe/stargates/{stargate_id}/

    destination = Column(Object)
    name = Column(String)
    position = Column(Object)
    stargate_id = Column(Integer)
    system_id = Column(Integer)
    type_id = Column(Integer)

    def __repr__(self):
        return 'destination={}, name={}, position={}, stargate_id={}, system_id={}, type_id={}'.format(self.destination, self.name, self.position, self.stargate_id, self.system_id, self.type_id)

class /universe/stars/{star_id}/(Base):
    __tablename__ = /universe/stars/{star_id}/

    age = Column(Integer)
    luminosity = Column(Float)
    name = Column(String)
    radius = Column(Integer)
    solar_system_id = Column(Integer)
    spectral_class = Column(String)
    temperature = Column(Integer)
    type_id = Column(Integer)

    def __repr__(self):
        return 'age={}, luminosity={}, name={}, radius={}, solar_system_id={}, spectral_class={}, temperature={}, type_id={}'.format(self.age, self.luminosity, self.name, self.radius, self.solar_system_id, self.spectral_class, self.temperature, self.type_id)

class /universe/stations/{station_id}/(Base):
    __tablename__ = /universe/stations/{station_id}/

    max_dockable_ship_volume = Column(Float)
    name = Column(String)
    office_rental_cost = Column(Float)
    owner = Column(Integer)
    position = Column(Object)
    race_id = Column(Integer)
    reprocessing_efficiency = Column(Float)
    reprocessing_stations_take = Column(Float)
    services = Column(Array)
    station_id = Column(Integer)
    system_id = Column(Integer)
    type_id = Column(Integer)

    def __repr__(self):
        return 'max_dockable_ship_volume={}, name={}, office_rental_cost={}, owner={}, position={}, race_id={}, reprocessing_efficiency={}, reprocessing_stations_take={}, services={}, station_id={}, system_id={}, type_id={}'.format(self.max_dockable_ship_volume, self.name, self.office_rental_cost, self.owner, self.position, self.race_id, self.reprocessing_efficiency, self.reprocessing_stations_take, self.services, self.station_id, self.system_id, self.type_id)

class /universe/structures/(Base):
    __tablename__ = /universe/structures/


    def __repr__(self):
        return ''.format()

class /universe/structures/{structure_id}/(Base):
    __tablename__ = /universe/structures/{structure_id}/

    name = Column(String)
    owner_id = Column(Integer)
    position = Column(Object)
    solar_system_id = Column(Integer)
    type_id = Column(Integer)

    def __repr__(self):
        return 'name={}, owner_id={}, position={}, solar_system_id={}, type_id={}'.format(self.name, self.owner_id, self.position, self.solar_system_id, self.type_id)

class /universe/system_jumps/(Base):
    __tablename__ = /universe/system_jumps/

    ship_jumps = Column(Integer)
    system_id = Column(Integer)

    def __repr__(self):
        return 'ship_jumps={}, system_id={}'.format(self.ship_jumps, self.system_id)

class /universe/system_kills/(Base):
    __tablename__ = /universe/system_kills/

    npc_kills = Column(Integer)
    pod_kills = Column(Integer)
    ship_kills = Column(Integer)
    system_id = Column(Integer)

    def __repr__(self):
        return 'npc_kills={}, pod_kills={}, ship_kills={}, system_id={}'.format(self.npc_kills, self.pod_kills, self.ship_kills, self.system_id)

class /universe/systems/(Base):
    __tablename__ = /universe/systems/


    def __repr__(self):
        return ''.format()

class /universe/systems/{system_id}/(Base):
    __tablename__ = /universe/systems/{system_id}/

    constellation_id = Column(Integer)
    name = Column(String)
    planets = Column(Array)
    position = Column(Object)
    security_class = Column(String)
    security_status = Column(Float)
    star_id = Column(Integer)
    stargates = Column(Array)
    stations = Column(Array)
    system_id = Column(Integer)

    def __repr__(self):
        return 'constellation_id={}, name={}, planets={}, position={}, security_class={}, security_status={}, star_id={}, stargates={}, stations={}, system_id={}'.format(self.constellation_id, self.name, self.planets, self.position, self.security_class, self.security_status, self.star_id, self.stargates, self.stations, self.system_id)

class /universe/types/(Base):
    __tablename__ = /universe/types/


    def __repr__(self):
        return ''.format()

class /universe/types/{type_id}/(Base):
    __tablename__ = /universe/types/{type_id}/

    capacity = Column(Float)
    description = Column(String)
    dogma_attributes = Column(Array)
    dogma_effects = Column(Array)
    graphic_id = Column(Integer)
    group_id = Column(Integer)
    icon_id = Column(Integer)
    market_group_id = Column(Integer)
    mass = Column(Float)
    name = Column(String)
    packaged_volume = Column(Float)
    portion_size = Column(Integer)
    published = Column(Boolean)
    radius = Column(Float)
    type_id = Column(Integer)
    volume = Column(Float)

    def __repr__(self):
        return 'capacity={}, description={}, dogma_attributes={}, dogma_effects={}, graphic_id={}, group_id={}, icon_id={}, market_group_id={}, mass={}, name={}, packaged_volume={}, portion_size={}, published={}, radius={}, type_id={}, volume={}'.format(self.capacity, self.description, self.dogma_attributes, self.dogma_effects, self.graphic_id, self.group_id, self.icon_id, self.market_group_id, self.mass, self.name, self.packaged_volume, self.portion_size, self.published, self.radius, self.type_id, self.volume)

class /wars/(Base):
    __tablename__ = /wars/


    def __repr__(self):
        return ''.format()

class /wars/{war_id}/(Base):
    __tablename__ = /wars/{war_id}/

    aggressor = Column(Object)
    allies = Column(Array)
    declared = Column(DateTime)
    defender = Column(Object)
    finished = Column(DateTime)
    id = Column(Integer)
    mutual = Column(Boolean)
    open_for_allies = Column(Boolean)
    retracted = Column(DateTime)
    started = Column(DateTime)

    def __repr__(self):
        return 'aggressor={}, allies={}, declared={}, defender={}, finished={}, id={}, mutual={}, open_for_allies={}, retracted={}, started={}'.format(self.aggressor, self.allies, self.declared, self.defender, self.finished, self.id, self.mutual, self.open_for_allies, self.retracted, self.started)

class /wars/{war_id}/killmails/(Base):
    __tablename__ = /wars/{war_id}/killmails/

    killmail_hash = Column(String)
    killmail_id = Column(Integer)

    def __repr__(self):
        return 'killmail_hash={}, killmail_id={}'.format(self.killmail_hash, self.killmail_id)

